
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
    const bioBody = document.getElementById('userbio');
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
            const bio = response.bio
            
            usernameBody.innerHTML = `@${username}`

            pictureBody.innerHTML += `<img src="${picture}" id="profilePic" class="AAAAAAAA" alt="profilepicture"></img>`
            pictureBody.innerHTML += `
            <div class="overlay">
              <a href="#" class="icon">
                <i class="fa fa-user"></i>
              </a>
            <div>`

            followersBody.innerHTML = `${followers} Seguidores`
            followingBody.innerHTML = `${following} Seguindo`
            bioBody.innerHTML = `${bio}`
            
            /**
             * Negocio do Post
             */

            const feed = response.feed
            console.log(feed)
            feed.forEach(element => {
                postBody.innerHTML += `
                <div class="postBlock border-top border-bottom">
                    <a href="/posts/${element.author}/${element.title}">
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
            /**
             * Negocio da sugestoes
             */

        },
        error: function(response){
            console.log(error)
        }
    })
    
    
})

