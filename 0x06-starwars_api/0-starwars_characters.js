#!/usr/bin/node

const process = require('process');

if (process.argv.length <= 2 || process.argv.length > 3) {
  console.log('Enter movie id => Movie ID - example: 3 = “Return of the Jedi”');
} else if (isNaN(process.argv[2])) {
  console.log('Enter movie id => Movie ID - example: 3 = “Return of the Jedi”');
} else if (process.argv[2] < 1 || process.argv[2] > 7) {
  console.log('Enter movie id between 1 and 7 => Movie ID - example: 3 = “Return of the Jedi”');
} else {
  const request = require('request');

  const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

  request(url, (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }

    const result = JSON.parse(body);
    const characterPromises = result.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, content) => {
          if (error) {
            reject(error);
            return;
          }
          const names = JSON.parse(content);
          resolve(names.name);
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.log(error);
      });
  });
}
