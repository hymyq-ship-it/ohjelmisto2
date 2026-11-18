'use strict';

const dogs = [];
for (let i = 0; i < 6; i++) {
  dogs.push(prompt(`Name of dog ${i + 1}:`));
}

dogs.sort();

let html = '<ul>';
for (let i = dogs.length - 1; i >= 0; i--) {
  html += `<li>${dogs[i]}</li>`;
}
html += '</ul>';

document.querySelector('#target').innerHTML = html;