const vuosi = Number(prompt("Anna vuosi:"));
let teksti = "";

if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || vuosi % 400 === 0) {
  teksti = vuosi + " on karkausvuosi.";
} else {
  teksti = vuosi + " ei ole karkausvuosi.";
}
document.querySelector('#target').innerHTML = teksti;