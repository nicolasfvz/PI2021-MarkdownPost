document.addEventListener('DOMContentLoaded', function() {
    const nomeInput = document.getElementById('nomeJS')
    console.log(nomeInput.innerHTML)
    /*
    console.log(profileBody)
    console.log(tituloBody)
    */
    
    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:8000/profiles/profile-json/${nomeInput.innerHTML}`,
        success: function(response){
            
            console.log(response)
            console.log(response.avatar)
            /*postBody.innerHTML = `${response.post.body}`*/

            /**
             * Get every element that is going to be modified
             */
            const usernameBody = document.getElementById('username');
            const followersBody = document.getElementById('followers');
            const followingBody = document.getElementById('following');
            const pictureBody = document.getElementById('foto');
            const bioBody = document.getElementById('userbio');
            const postBody = document.getElementById('postsItems');



            /*
            * Negocio do Profile
            */     
            console.log(response.avatar)
            usernameBody.innerHTML = `@${response.name}`
            pictureBody.innerHTML += `<img src="${response.avatar}" id="profilePic" class="AAAAAAAA" alt="profilepicture"></img>`
            followersBody.innerHTML = `${response.followers} Seguidores`
            followingBody.innerHTML = `${response.following} Seguindo`
            bioBody.innerHTML = `${response.bio}`
            
            /**
             * Negocio do feed
             */

             response.feed.forEach(element => {
                postBody.innerHTML += `
                <div class="postBlock border-top border-bottom">
                    <a href="/posts/${response.name}/${element}">
                        <div class="postElements d-flex py-3">
                            <div class="postUserPic">
                              <img src="${response.avatar}" alt="icon">
                            </div> 
                
                            <div class="d-flex">
                              <p class="medium my-auto"><strong>@${response.name}</strong></p>
                            </div>
                
                            <div class="d-flex flex-grow-1 justify-content-center">
                              <h3 class="fs-5 my-auto">${element}</h3>
                            </div>	

                        </div>
                    </a>
                </div>
              `
            })
            
        },
        error: function(response){
            console.log(error)
        }
    })
    
})