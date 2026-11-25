const form = document.getElementById('search-form');
const input = document.getElementById('query');
const resultsDiv = document.getElementById('results');
const statusEl = document.getElementById('status');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const value = input.value.trim();
  if (!value) return;

  statusEl.textContent = 'Haetaan...';
  resultsDiv.innerHTML = '';

  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${encodeURIComponent(value)}`);
    const data = await response.json();
    console.log(data); // koko tulos konsoliin (3p vaatimus)

    if (data.length === 0) {
      statusEl.textContent = 'Ei tuloksia.';
      return;
    }
    statusEl.textContent = `Löytyi ${data.length} tulosta.`;

    data.forEach((tvShow) => {
      const article = document.createElement('article');

      const h2 = document.createElement('h2');
      h2.textContent = tvShow.show.name;

      const link = document.createElement('a');
      link.href = tvShow.show.url;
      link.textContent = tvShow.show.url;
      link.target = '_blank';

      const img = document.createElement('img');
      // Ternary / if-else oletuskuvalle - ei pelkkä ?.
      if (tvShow.show.image && tvShow.show.image.medium) {
        img.src = tvShow.show.image.medium;
      } else {
        img.src = 'https://placehold.co/210x295?text=Not%20Found';
      }
      img.alt = tvShow.show.name;

      const summaryDiv = document.createElement('div');
      summaryDiv.innerHTML = tvShow.show.summary || 'Ei kuvausta.';

      article.append(h2, link, img, summaryDiv);
      resultsDiv.appendChild(article);
    });
  } catch (error) {
    console.error(error);
    statusEl.textContent = 'Virhe haussa. Yritä uudelleen.';
  }
});