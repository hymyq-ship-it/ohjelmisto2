const maara = Number(prompt("Montako noppaa heitetään?"));
let summa = 0;

for (let i = 0; i < maara; i++) {
  const heitto = Math.floor(Math.random() * 6) + 1;
  summa = summa + heitto;
}
document.querySelector('#target').innerHTML = "Summa: " + summa;