document.addEventListener('DOMContentLoaded', function() {
    const tituloBody = document.getElementById('titulo');
    const profileBody = document.getElementById('profile');

    console.log(profileBody.innerHTML)
    console.log(tituloBody.innerHTML)
    

    $.ajax({
        type: 'GET',
        url: `/profiles/my-profile-json/`,
        success: function(response){
            console.log(response)
            
            
        },
        error: function(response){
            console.log(error)
        }
    })

})