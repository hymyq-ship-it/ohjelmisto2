function nayta() {
  const h = document.getElementById("hytti").value;
  let teksti;
  if (h === "LUX") teksti = "LUX on parvekkeellinen hytti yläkannella.";
  else if (h === "A") teksti = "A on ikkunallinen hytti autokannen yläpuolella.";
  else if (h === "B") teksti = "B on ikkunaton hytti autokannen yläpuolella.";
  else if (h === "C") teksti = "C on ikkunaton hytti autokannen alapuolella.";
  else teksti = "Virheellinen hyttiluokka";
  document.getElementById("tulos").textContent = teksti;
}