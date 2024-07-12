#!/usr/bin/node

const { error } = require('console');
const { request } = require('http');
const process = require('process');
const { json } = require('stream/consumers');
if(process.argv.length <= 2 || process.argv.length > 3)
    {
        console.log("Enter movie id => Movie ID - example: 3 = “Return of the Jedi”");
    }
else if(isNaN(process.argv[2]))
    {
        console.log("Enter movie id => Movie ID - example: 3 = “Return of the Jedi”");
    }
else if(process.argv[2] <0 || process.argv[2] > 7)
{
    console.log("Enter movie id between 1 and 7 => Movie ID - example: 3 = “Return of the Jedi”");
}
else
{
    const request = require('request');
    
    let url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

    request(url, (error,response, body) => 
        {
            if(error)
                {
                    console.log(error);
                }
            //console.log(response.statuscode);
            //console.log(body);
            let result = JSON.parse(body);
            
            for(let i = 0; i < result.characters.length; i ++)
                {
                    request(result.characters[i], (error,response,content) =>
                        {
                            if(error)
                            {
                                console.log(error);
                            }
                            let names = JSON.parse(content);
                            console.log(names.name);
                            
                        });
                }
        });
}