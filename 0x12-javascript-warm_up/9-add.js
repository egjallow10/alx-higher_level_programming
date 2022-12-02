#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
console.log(process.argv.length === 4 ? add(parseInt(process.argv[2]), parseInt(process.argv[3])) : 'NaN');
