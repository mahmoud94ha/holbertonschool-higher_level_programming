#!/usr/bin/node

// This script computes the number of tasks completed by user id.
const request = require('request');
const argv = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + argv + '/';

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    });
  }
});
