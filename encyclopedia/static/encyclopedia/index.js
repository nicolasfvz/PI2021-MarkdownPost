document.addEventListener('DOMContentLoaded', function() {
    fetch('http://127.0.0.1:8000/wiki/api')
    .then(response => response.json())
    .then(data => {
        let txt = "";
        const lenL = data.title.length; 
        for (let i = 0; i < lenL; i++) {
            txt += `<a href="/wiki/${data.title[i]}">
            <div class="d-flex text-muted pt-3"> 
                  <p class="pb-3 mb-0 small lh-sm border-bottom">
                    <strong class="d-block text-gray-dark">@username</strong>
                    ${data.title[i]}
                  </p>
            </div>
            </a>`
          }
        document.querySelector('#postagem').innerHTML = txt;
    });
});
