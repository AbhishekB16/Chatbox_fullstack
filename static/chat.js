$(document).ready(function(){
    var csrf=$("input[name=csrfmiddlewaretoken]").val();

    // $("#4").click(function(){
    //     $.ajax({
    //         url:'/get',
    //         type:'get',
    //         data:{
    //             // button_text:$(this).text()
    //             button_text:$(this).text()
    //         },
            
    //         success: function(response){
                
    //             $("#4").text(response.seconds)
    //             $("#seconds").append('<li>'+response.seconds+'</li>')
    //         }
            
    //     });
        
    // });
    $("#2").on('click',function(){
        $.ajax({
            url:'/post',
            type:'post',
            data:{
                // text: $(this).text(),
                // text:"this is 2211",
                text: $("#chat_msg").val(),
                csrfmiddlewaretoken :csrf
            },
            success: function(response){
                $("#chat_1").append('<p>'+response.data+'</p>')
            }
        })
    });

});