#!/usr/bin/node

import fs from 'fs';
import { argv } from 'process';
const fileName = argv[1];
fs.readFile(`./${fileName}`, 'utf-8', (error, data) => {
  if (error) {
    throw error;
  }
  console.log(data);
});
