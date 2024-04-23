#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }
  
  const todos = JSON.parse(body);
  const completedTasksByUserId = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasksByUserId[userId]) {
        completedTasksByUserId[userId]++;
      } else {
        completedTasksByUserId[userId] = 1;
      }
    }
  });
  
  console.log(completedTasksByUserId);
});
