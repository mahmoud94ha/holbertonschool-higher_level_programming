#!/usr/bin/node

const Ha = require('Ha');
Ha.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(err || data);
});
