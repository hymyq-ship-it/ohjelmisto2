'use strict';

const count = Number(prompt('How many participants?'));
const names = [];

for (let i = 0; i < count; i++) {
  const name = prompt(`Name of participant ${i + 1}:`);
  names.push(name);
}

names.sort();

let html = '<ol>';
for (let i = 0; i < names.length; i++) {
  html += `<li>${names[i]}</li>`;
}
html += '</ol>';

document.querySelector('body').innerHTML = html;