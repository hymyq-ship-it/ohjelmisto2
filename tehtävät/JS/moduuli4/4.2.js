const randomBtn = document.getElementById('random-btn');
const form = document.getElementById('search-form');
const input = document.getElementById('query');
const resultsDiv = document.getElementById('results');
const statusEl = document.getElementById('status');

function showJoke(jokeText) {
  const article = document.createElement('article');
  const p = document.createElement('p');
  p.textContent = jokeText;
  article.appendChild(p);
  resultsDiv.appendChild(article);
}

// Satunnainen vitsi - vain value konsoliin
randomBtn.addEventListener('click', async () => {
  resultsDiv.innerHTML = '';
  statusEl.textContent = 'Haetaan...';
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const data = await response.json();
    console.log(data.value);
    statusEl.textContent = '';
    showJoke(data.value);
  } catch (e) {
    console.error(e);
    statusEl.textContent = 'Virhe haussa.';
  }
});

// Haku hakusanalla
form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const value = input.value.trim();
  if (!value) return;
  resultsDiv.innerHTML = '';
  statusEl.textContent = 'Haetaan...';
  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(value)}`);
    const data = await response.json();
    console.log(data);
    if (data.total === 0) {
      statusEl.textContent = 'Ei vitsejä tällä hakusanalla.';
      return;
    }
    statusEl.textContent = `Löytyi ${data.total} vitsiä.`;
    data.result.forEach((joke) => showJoke(joke.value));
  } catch (e) {
    console.error(e);
    statusEl.textContent = 'Virhe haussa.';
  }
});