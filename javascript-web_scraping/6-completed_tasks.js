#!/usr/bin/node

const axios = require('axios');
let tab;
async function start () {
  await axios({
    method: 'GET',
    url: process.argv[2]
  }).then(res => {
    if (res) {
      tab = res.data;
    }
  });
  const usertask = [];
  for (let i = 0; i < tab.length; i++) {
    if (tab[i].completed) {
      if (usertask[tab[i].userId] == null) {
        usertask[tab[i].userId] = 0;
      }
      usertask[tab[i].userId] += 1;
    }
  }
  const element = {};
  for (let i = 0; i < usertask.length; i++) {
    if (usertask[i] != null) {
      element[i] = usertask[i];
    }
  }
  console.log(element);
}
start();
