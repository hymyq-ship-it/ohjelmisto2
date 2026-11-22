const target = document.getElementById('target');
const texts = ['First item', 'Second item', 'Third item'];

for (let i = 0; i < texts.length; i++) {
  const li = document.createElement('li');
  li.textContent = texts[i];
  if (i === 1) {
    li.classList.add('my-item');
  }
  target.appendChild(li);
}