
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
            
            usernameBody.innerHTML = `@${response.username}`
            pictureBody.innerHTML += `<img src="${response.avatar}" id="profilePic" class="AAAAAAAA" alt="profilepicture"></img>`
            followersBody.innerHTML = `${response.followers} Seguidores`
            followingBody.innerHTML = `${response.following} Seguindo`
            bioBody.innerHTML = `${response.bio}`

            /*
            pictureBody.innerHTML += `
            <div class="overlay">
              <a href="#" class="icon">
                <i class="fa fa-user"></i>
              </a>
            <div>`*/


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
            /**
             * <div class="d-flex text-muted pt-3">
                            <div class="row mb-2 align-items-center">
                                <div class="col2">
                                    <img src="${element.avatar}" class="avatar" alt="${element.username}">
                                </div>
                            </div>
                            <p class="pb-3 mb-0 small lh-sm border-bottom">
                              <strong class="d-block text-gray-dark"> @${element.username}</strong>
                               ${element.bio}
                            </p>
                        </div>
             */
            
            const butao = document.getElementById('recomendacoes-butao');
            const toFollowModalBody = document.getElementById('profileSuggestions');

                
            const data = response.profiles_to_follow_list
            var aux = 0
            console.log(data)
            data.forEach(element => {
                console.log(element.avatar)
                toFollowModalBody.innerHTML += `
                <div class="modal-profile d-flex justify-content-evenly align-items-center">
                    <img alt="icon" class="avatar" src="${element.avatar}">
                    <span>@${element.username}</span>
                    <input class="form-check-input mt-0" id="checkbox${aux}" type="checkbox" value="${element.username}" aria-label="Checkbox for following text input">
                    
                </div>
                `
                aux++;
            });
            
           
            
                        
    

        },
        error: function(response){
            console.log(error)
        }
    })
    
    
})

