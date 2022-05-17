#!/usr/bin/node
const fs = required('fs');

const data = process.argv[3];

fs.wirteFile(process.argv[2], data, function (err, data) {
	if (err) console.log(err);
}Ã);
