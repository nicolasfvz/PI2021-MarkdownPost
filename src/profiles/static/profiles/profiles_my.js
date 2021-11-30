
document.addEventListener('DOMContentLoaded', function() {
    /**
     * Carregar a pagina inteira via javascript
     */
    const usernameBody = document.getElementById('username');
    const followersBody = document.getElementById('followers');
    const followingBody = document.getElementById('following');
    const pictureBody = document.getElementById('foto');
     $.ajax({
        type: 'GET',
        url: '/profiles/my-profile-json/',
        success: function(response){
            
        const username = response.username
        const picture = response.avatar
        const followers = response.followers
        const following = response.following
        
        console.log(picture)
        usernameBody.innerHTML = `@${username}`
        pictureBody.innerHTML = `<img src="${picture}" id="profilePic" class="avatarPicture" alt="profilepicture"></img>`
        followersBody.innerHTML = `${followers} Seguidores`
        followingBody.innerHTML = `${following} Seguindo`
                
            
            
        },
        error: function(response){
            console.log(error)
        }
    })
    
    /* Negocio do botão */ 
    const butao = document.getElementById('recomendacoes-butao');
    const toFollowModalBody = document.getElementById('to-follow-modal-content');
    const spinnerModalBody = document.getElementById('spiner-splendi');
    let toFollowLoaded = false
    
    butao.addEventListener('click', ()=>{
        $.ajax({
            type: 'GET',
            url: '/profiles/my-profile-json/',
            success: function(response){
                if(!toFollowLoaded){
                    const data = response.profiles_to_follow_list

                    setTimeout(function() {

                        spinnerModalBody.innerHTML = ''
                        console.log(response)
                        data.forEach(element => {
                            console.log(element.avatar)
                            toFollowModalBody.innerHTML += `
                            <div class="d-flex text-muted pt-3">
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
                            `
                        });

                    }, 2000)
                    toFollowLoaded = true
                }
                
            },
            error: function(response){
                console.log(error)
            }
        })
    })
    
})

