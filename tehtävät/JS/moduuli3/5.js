const section = document.querySelector('section');

for (let i = 0; i < picArray.length; i++) {
  const pic = picArray[i];

  const article = document.createElement('article');
  article.classList.add('card');

  const h2 = document.createElement('h2');
  h2.textContent = pic.title;

  const figure = document.createElement('figure');
  const img = document.createElement('img');
  img.src = pic.medium_image;
  img.alt = pic.title;

  const figcaption = document.createElement('figcaption');
  figcaption.textContent = pic.caption;

  const p = document.createElement('p');
  p.textContent = pic.description;

  figure.appendChild(img);
  figure.appendChild(figcaption);

  article.appendChild(h2);
  article.appendChild(figure);
  article.appendChild(p);

  section.appendChild(article);
}