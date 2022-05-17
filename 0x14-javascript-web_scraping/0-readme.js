#!/usr/bin/node
const fileList = event.target.files;
let fileContent = "";

const fr = new FileReader();
fr.onload = () => {
  fileContent = fr.result;
  console.log('Commands', fileContent);
}

fr.readAsText(fileList[0]);
