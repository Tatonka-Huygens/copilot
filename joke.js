function getJoke() {
    var category = document.getElementById('category').value;
    fetch('http://localhost:5000/display_joke/' + category)
        .then(response => response.json())
        .then(data => {
            document.getElementById('joke').innerText = data.joke;
        });
    return false;
}

function searchJoke(event) {
    event.preventDefault();
    var term = document.getElementById('term').value;
    fetch('http://localhost:5000/search_joke/' + term)
        .then(response => response.json())
        .then(data => {
            document.getElementById('search-joke').innerText = data.joke;
        });
}