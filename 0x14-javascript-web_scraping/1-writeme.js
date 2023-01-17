#!/usr/bin/node
const fs = require('fs');
const toWrite = process.argv[3];
fs.writeFile(process.argv[2], toWrite, function read (err) {
  if (err) {
    console.log(err);
  }
});
