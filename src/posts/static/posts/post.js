document.addEventListener('DOMContentLoaded', function() {
    const profileBody = document.getElementById('profile');
    const tituloBody = document.getElementById('titulo');
    

    console.log(profileBody)
    console.log(tituloBody)
    

    $.ajax({
        type: 'GET',
        url: `http://127.0.0.1:8000/posts/api/?profile=${profileBody.innerHTML}&post=${tituloBody.innerHTML}`,
        success: function(response){
            console.log(response)
            
            
        },
        error: function(response){
            console.log(error)
        }
    })

})