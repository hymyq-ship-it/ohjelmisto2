const a = Number(prompt("Anna 1. luku:"));
const b = Number(prompt("Anna 2. luku:"));
const c = Number(prompt("Anna 3. luku:"));

const summa = a + b + c;
const tulo = a * b * c;
const keskiarvo = summa / 3;

document.querySelector('#target').innerHTML = "Summa: " + summa + ", Tulo: " + tulo + ", Keskiarvo: " + keskiarvo;