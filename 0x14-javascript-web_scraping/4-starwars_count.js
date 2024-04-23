#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  const movies = JSON.parse(body).results;
  let count = 0;
  movies.forEach((movie) => {
    const cast = movie.characters;
    if (cast.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });
  console.log(count);
});
