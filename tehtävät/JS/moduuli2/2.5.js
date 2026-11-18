'use strict';

const numbers = [];
let num;
let duplicate = false;

while (!duplicate) {
  num = Number(prompt('Enter a number:'));

  if (numbers.includes(num)) {
    console.log(`Number ${num} has already been given.`);
    duplicate = true;
  } else {
    numbers.push(num);
  }
}

numbers.sort((a, b) => a - b);

console.log('All given numbers in ascending order:');
for (const n of numbers) {
  console.log(n);
}