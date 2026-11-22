function tarkista() {
  const p = Number(document.getElementById("pituus").value);
  if (p < 37) {
    document.getElementById("tulos").textContent =
      `Laske kuha takaisin järveen! Alimmasta sallitusta pyyntimitasta puuttuu ${37 - p} cm.`;
  } else {
    document.getElementById("tulos").textContent = "Kuha on mitallinen.";
  }
}