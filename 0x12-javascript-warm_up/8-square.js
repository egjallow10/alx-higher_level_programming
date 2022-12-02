#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (times) {
  for (const ch of 'X'.repeat(times)) {
    console.log(ch.repeat(times));
  }
}
