'use strict';

const dogs = [];

for (let i = 0; i < 6; i++) {
  const name = prompt(`Name of dog ${i + 1}:`);
  dogs.push(name);
}

// sort() -> aakkosjärjestys, reverse() kääntää sen
// Tehtävässä ei kielletty reverse() käyttöä tässä, vain tehtävässä 1
dogs.sort().reverse();

let html = '<ul>';
for (const dog of dogs) {
  html += `<li>${dog}</li>`;
}
html += '</ul>';

document.querySelector('body').innerHTML = html;