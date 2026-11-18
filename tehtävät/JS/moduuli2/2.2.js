'use strict';

const count = Number(prompt('How many participants?'));
const names = [];
for (let i = 0; i < count; i++) {
  names.push(prompt(`Name of participant ${i + 1}:`));
}

names.sort();

let html = '<ol>';
for (const name of names) {
  html += `<li>${name}</li>`;
}
html += '</ol>';

document.querySelector('#target').innerHTML = html;