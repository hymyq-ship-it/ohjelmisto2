'use strict';

const numbers = [];
let num;
do {
  num = Number(prompt('Enter a number (0 stops):'));
  if (num !== 0) {
    numbers.push(num);
  }
} while (num !== 0);

numbers.sort((a, b) => b - a);

console.log('Numbers from largest to smallest:');
for (const n of numbers) {
  console.log(n);
}