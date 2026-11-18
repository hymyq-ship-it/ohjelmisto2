'use strict';

function diceRoll(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const sides = Number(prompt('How many sides on the dice?'));
let result;
let html = '<ul>';

do {
  result = diceRoll(sides);
  html += `<li>${result}</li>`;
} while (result !== sides);

html += '</ul>';
document.querySelector('body').innerHTML = html;