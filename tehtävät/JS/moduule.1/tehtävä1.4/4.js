const nimi = prompt("Anna nimesi:");
const arpa = Math.floor(Math.random() * 4) + 1;
let tupa = "";

if (arpa === 1) {
  tupa = "Gryffindor";
} else if (arpa === 2) {
  tupa = "Slytherin";
} else if (arpa === 3) {
  tupa = "Hufflepuff";
} else {
  tupa = "Ravenclaw";
}
document.querySelector('#target').innerHTML = nimi + ", you are " + tupa + ".";