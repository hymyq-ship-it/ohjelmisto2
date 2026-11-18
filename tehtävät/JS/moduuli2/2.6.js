'use strict';

function diceRoll() {
  return Math.floor(Math.random() * 6) + 1;
}

let result;
let html = '<ul>';

do {
  result = diceRoll();
  html += `<li>${result}</li>`;
} while (result !== 6);

html += '</ul>';
document.querySelector('body').innerHTML = html;