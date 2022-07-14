const apiUrl = "https://pokeapi.co/api/v2/pokemon/";
const input = document.querySelector(".pokemon-input");
const pokemonName = document.querySelector(".pokemon-name");
const pokemonImage = document.querySelector(".pokemon-image");

function getPokemonData() {
    axios.get(apiUrl + input.value)
    .then(function (response) {
        pokemonName.innerHTML = response.data.forms[0].name;
        pokemonImage.src = response.data.sprites.front_default;
    })
    .catch(function (error) {
        pokemonName.innerHTML = "(An error has occurred.)";
        pokemonImage.src = "";
    });
}

const button = document.querySelector(".pokemon-button");
button.addEventListener("click", getPokemonData);