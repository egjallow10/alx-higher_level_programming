#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing size');
} else if (times > 0) {
  for (let i = 0; i < times; i++) {
    let value = '';
    for (let j = 0; j < times; j++) {
      value += 'X';
    }
    console.log(value);
  }
}
