#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (error, data1) => {
  if (error) {
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (error, data2) => {
    if (error) {
      return;
    }
    const concatenatedData = data1 + data2;
    fs.writeFile(destinationFile, concatenatedData, 'utf8', (error) => {
      if (error) {
        return;
      }
    });
  });
});
