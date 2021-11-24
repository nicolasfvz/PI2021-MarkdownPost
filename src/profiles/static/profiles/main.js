
document.addEventListener('DOMContentLoaded', function() {

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
                    const data = response.data

                    setTimeout(function() {

                        spinnerModalBody.innerHTML = ''
                        data.forEach(element => {
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

