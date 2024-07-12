#!/usr/bin/node

const { error } = require('console');
const { request } = require('http');
const process = require('process');

if (process.argv.length <= 2 || process.argv.length > 3) {
    console.log("Enter movie id => Movie ID - example: 3 = “Return of the Jedi”");
} else if (isNaN(process.argv[2])) {
    console.log("Enter movie id => Movie ID - example: 3 = “Return of the Jedi”");
} else if (process.argv[2] < 1 || process.argv[2] > 7) {
    console.log("Enter movie id between 1 and 7 => Movie ID - example: 3 = “Return of the Jedi”");
} else {
    const request = require('request');
    
    let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

    request(url, (error, response, body) => {
        if (error) {
            console.log(error);
            return;
        }
        
        let result = JSON.parse(body);
        let characterPromises = result.characters.map((characterUrl) => {
            return new Promise((resolve, reject) => {
                request(characterUrl, (error, response, content) => {
                    if (error) {
                        reject(error);
                        return;
                    }
                    let names = JSON.parse(content);
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
