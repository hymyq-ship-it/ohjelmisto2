function tarkista() {
  const v = Number(document.getElementById("vuosi").value);
  const onKarkaus = (v % 4 === 0 && v % 100 !== 0) || (v % 400 === 0);
  document.getElementById("tulos").textContent =
    onKarkaus ? `Vuosi ${v} on karkausvuosi.` : `Vuosi ${v} ei ole karkausvuosi.`;
}