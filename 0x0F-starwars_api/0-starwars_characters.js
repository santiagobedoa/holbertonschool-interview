const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else if (response.statusCode !== 200) {
    console.error(`HTTP Status Code: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error: ${error}`);
        } else if (response.statusCode !== 200) {
          console.error(`HTTP Status Code: ${response.statusCode}`);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
