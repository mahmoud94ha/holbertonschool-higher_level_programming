#!/usr/bin/node

// This script computes the number of tasks completed by user id.
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  const charactersCount = characters.length;
  let charactersLoaded = 0;
  const characterNames = new Array(charactersCount);
  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      characterNames[index] = JSON.parse(body).name;

      charactersLoaded++;
      if (charactersLoaded === charactersCount) {
        characterNames.forEach((name) => {
          console.log(name);
        });
      }
    });
  });
});
