
function myfunc() {
$(document).on('submit', '#post-form', function(e){
    e.preventDefault();
    $.ajax({
        type:'GET',
        url:'api/data',
        data: {
            fname:$('#x').val(),
            // csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
    success: function(data) {
        $('h2').html(data);
        console.log(data);
    }
    })
})
}

window.myfunc = myfunc;