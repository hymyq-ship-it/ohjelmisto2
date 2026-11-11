const haluaako = confirm("Should I calculate the square root?");

if (haluaako) {
  const luku = Number(prompt("Anna luku:"));
  if (luku < 0) {
    document.querySelector('#target').innerHTML = "The square root of a negative number is not defined";
  } else {
    document.querySelector('#target').innerHTML = "Neliöjuuri on " + Math.sqrt(luku);
  }
} else {
  document.querySelector('#target').innerHTML = "The square root is not calculated.";
}