#!/usr/bin/node
const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(sourceFile1, 'utf8', (error, data1) => {
  if (error) {
    console.error(`Error reading ${sourceFile1}:`, error);
    return;
  }

  fs.readFile(sourceFile2, 'utf8', (error, data2) => {
    if (error) {
      console.error(`Error reading ${sourceFile2}:`, error);
      return;
    }
    
    const concatenatedData = data1 + data2;

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (error) => {
      if (error) {
        console.error(`Error writing to ${destinationFile}:`, error);
        return;
      }

      console.log(`Successfully concatenated ${sourceFile1} and ${sourceFile2} into ${destinationFile}`);
    });
  });
});
