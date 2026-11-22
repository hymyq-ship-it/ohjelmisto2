function tarkista() {
  const s = document.getElementById("sukupuoli").value;
  const hb = Number(document.getElementById("hb").value);
  let tulos;
  if (s === "nainen") {
    if (hb < 117) tulos = "Hemoglobiiniarvo on alhainen.";
    else if (hb > 175) tulos = "Hemoglobiiniarvo on korkea.";
    else tulos = "Hemoglobiiniarvo on normaali.";
  } else {
    if (hb < 134) tulos = "Hemoglobiiniarvo on alhainen.";
    else if (hb > 195) tulos = "Hemoglobiiniarvo on korkea.";
    else tulos = "Hemoglobiiniarvo on normaali.";
  }
  document.getElementById("tulos").textContent = tulos;
}