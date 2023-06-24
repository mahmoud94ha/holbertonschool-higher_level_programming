#!/usr/bin/node

// This script computes the number of tasks completed by user id.
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const todos = JSON.parse(body);
    const completedTasksCount = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasksCount[todo.userId]) {
          completedTasksCount[todo.userId]++;
        } else {
          completedTasksCount[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksCount);
  }
});
