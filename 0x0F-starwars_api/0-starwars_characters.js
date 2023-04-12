const request = require("request-promise");

const movieID = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieID}/`;

request(apiUrl)
  .then((movieData) => {
    const characters = JSON.parse(movieData).characters;
    const characterPromises = characters.map((characterUrl) => {
      return request(characterUrl);
    });
    return Promise.all(characterPromises);
  })
  .then((characterData) => {
    characterData.forEach((character) => {
      console.log(JSON.parse(character).name);
    });
  })
  .catch((error) => {
    console.error(`Error: ${error}`);
  });
