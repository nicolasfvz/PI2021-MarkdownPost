
/**
 * Wait until the page is loades
 */
document.addEventListener('DOMContentLoaded', function() {
    
    /**
     * Get every element that is going to be modified
     */
    const usernameBody = document.getElementById('username');
    const followersBody = document.getElementById('followers');
    const followingBody = document.getElementById('following');
    const pictureBody = document.getElementById('foto');
    const postBody = document.getElementById('postsItems');

    /**
     *  Send a request to get the data
     */
    $.ajax({
        type: 'GET',
        url: '/profiles/my-profile-json/',
        success: function(response){
            console.log(response)

            /*
            * Negocio do Profile
            */     
            const username = response.username
            const picture = response.avatar
            const followers = response.followers
            const following = response.following
            
            usernameBody.innerHTML = `@${username}`
            pictureBody.innerHTML += `<img src="${picture}" id="profilePic" class="AAAAAAAA" alt="profilepicture"></img>`
            // pictureBody.innerHTML += `<img class="cogOverlay" src="https://dictionary.cambridge.org/pt/images/thumb/cog_noun_002_07459.jpg?version=5.0.199" alt="Editar Perfil">`
            followersBody.innerHTML = `${followers} Seguidores`
            followingBody.innerHTML = `${following} Seguindo`
            
            /**
             * Negocio do Post
             */

            const feed = response.feed
            console.log(feed)
            feed.forEach(element => {
                postBody.innerHTML += `
                <div class="postBlock border-top border-bottom">
                    <a href="#">
                        <div class="postElements d-flex py-3">
                            <div class="postUserPic">
                              <img src="${element.avatar}" alt="icon">
                            </div> 
                
                            <div class="d-flex">
                              <p class="medium my-auto"><strong>@${element.author}</strong></p>
                            </div>
                
                            <div class="d-flex flex-grow-1 justify-content-center">
                              <h3 class="fs-5 my-auto">${element.title}</h3>
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

