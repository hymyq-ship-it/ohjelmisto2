// students-taulukko tulee valmiina, esim. [{id:'2345768', name:'John'}, ...]
// Jos se on eri muodossa, kerro niin korjaan.
const target = document.getElementById('target');

for (let i = 0; i < students.length; i++) {
  const option = document.createElement('option');
  option.value = students[i].id;
  option.textContent = students[i].name;
  target.appendChild(option);
}