#!/usr/bin/node

// This script computes the number of tasks completed by user id.
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    const printCharacterName = (characterUrl) => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Status:', response.statusCode);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    };
    characterUrls.forEach(printCharacterName);
  }
});
