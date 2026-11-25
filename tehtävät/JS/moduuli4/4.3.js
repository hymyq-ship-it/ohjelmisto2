const form = document.getElementById('route-form');
const addressInput = document.getElementById('address');
const statusEl = document.getElementById('status');
const tripInfo = document.getElementById('trip-info');
const legsDiv = document.getElementById('legs');

const SCHOOL = { name: 'Karaportti 2, Espoo', lat: 60.2239, lon: 24.7589 };

// Kartta
let map;
let routeLayer;

function initMap() {
  map = L.map('map').setView([60.224, 24.759], 13);
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap'
  }).addTo(map);
  L.marker([SCHOOL.lat, SCHOOL.lon]).addTo(map).bindPopup(SCHOOL.name);
}
window.addEventListener('load', initMap);

async function geocode(text) {
  const res = await fetch(`https://api.digitransit.fi/geocoding/v1/search?text=${encodeURIComponent(text)}&size=1`);
  const data = await res.json();
  if (!data.features || data.features.length === 0) throw new Error('Osoitetta ei löytynyt');
  const [lon, lat] = data.features[0].geometry.coordinates;
  return { lat, lon, label: data.features[0].properties.label };
}

function formatTime(ms) {
  return new Date(ms).toLocaleTimeString('fi-FI', { hour: '2-digit', minute: '2-digit' });
}

// Polyline decode (Google polyline)
function decodePolyline(str) {
  let index = 0, lat = 0, lng = 0, coords = [];
  while (index < str.length) {
    let b, shift = 0, result = 0;
    do { b = str.charCodeAt(index++) - 63; result |= (b & 0x1f) << shift; shift += 5; } while (b >= 0x20);
    const dlat = (result & 1) ? ~(result >> 1) : (result >> 1); lat += dlat;
    shift = 0; result = 0;
    do { b = str.charCodeAt(index++) - 63; result |= (b & 0x1f) << shift; shift += 5; } while (b >= 0x20);
    const dlng = (result & 1) ? ~(result >> 1) : (result >> 1); lng += dlng;
    coords.push([lat / 1e5, lng / 1e5]);
  }
  return coords;
}

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const address = addressInput.value.trim();
  statusEl.textContent = 'Haetaan reittiä...';
  tripInfo.innerHTML = ''; legsDiv.innerHTML = '';
  if (routeLayer) map.removeLayer(routeLayer);

  try {
    const from = await geocode(address);
    const query = `
      { plan(from: {lat: ${from.lat}, lon: ${from.lon}} to: {lat: ${SCHOOL.lat}, lon: ${SCHOOL.lon}} numItineraries: 1) {
        itineraries { startTime endTime duration legs { mode from { name } to { name } duration distance legGeometry { points } } }
      } }`;
    const res = await fetch('https://api.digitransit.fi/routing/v2/hsl/gtfs/v1', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    });
    const json = await res.json();
    const it = json.data.plan.itineraries[0];
    if (!it) throw new Error('Reittiä ei löytynyt');

    statusEl.textContent = '';
    tripInfo.innerHTML = `<strong>Lähtö:</strong> ${formatTime(it.startTime)} &nbsp; <strong>Perillä:</strong> ${formatTime(it.endTime)} &nbsp; <strong>Kesto:</strong> ${Math.round(it.duration / 60)} min<br><strong>Mistä:</strong> ${from.label} &nbsp; <strong>Minne:</strong> ${SCHOOL.name}`;

    // Kartta: merkki + reitti
    const startMarker = L.marker([from.lat, from.lon]).bindPopup(from.label);
    const endMarker = L.marker([SCHOOL.lat, SCHOOL.lon]).bindPopup(SCHOOL.name);
    const lines = [];
    it.legs.forEach((leg) => {
      if (leg.legGeometry && leg.legGeometry.points) {
        lines.push(L.polyline(decodePolyline(leg.legGeometry.points), { weight: 5 }));
      }
      const div = document.createElement('div');
      div.textContent = `${leg.mode} - ${leg.from.name} -> ${leg.to.name} (${Math.round(leg.duration / 60)} min)`;
      legsDiv.appendChild(div);
    });
    routeLayer = L.layerGroup([startMarker, endMarker, ...lines]).addTo(map);
    map.fitBounds(routeLayer.getBounds(), { padding: [30, 30] });
  } catch (err) {
    console.error(err);
    statusEl.textContent = 'Virhe: ' + err.message;
  }
});