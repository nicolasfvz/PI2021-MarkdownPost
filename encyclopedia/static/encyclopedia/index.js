document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:8000/wiki/api')
    .then(response => response.json())
    .then(data => {
        let txt = "";
        const lenL = data.title.length; 
        for (let i = 0; i < lenL; i++) {
            txt += ` <h1>${data.title[i]}</h1>`
          }
        document.querySelector('#postagem').innerHTML = txt;
    });
});
