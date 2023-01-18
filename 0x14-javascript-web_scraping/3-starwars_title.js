#!/usr/bin/node
/** Script tp print the tittle from the avialable api */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(`${url}${process.argv[2]}`, (err, data) => {
  if (err) {
    console.log(err);
  }
  const mytitle = JSON.parse(data.body);
  console.log(mytitle.title);
});
