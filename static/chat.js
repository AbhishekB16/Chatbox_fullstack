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
    
    $("#chat_1").hide();
    $("#main1").hide();
    $("#6").on('click',function(){
        $("#main1").show();
    })
    $("#2").on('click',function(){
        
        $.ajax({
            url:'/post',
            type:'post',
            data:{
                // text: $(this).text(),
                // text:"this is 2211",
                email:$("#myvar").val(),
                email_to:$(".myvar2").val(),
                text: $("#chat_msg").val(),
                csrfmiddlewaretoken :csrf
            },
            success: function(response){
                $("#chat_2").append('<p>'+response.msg11+'</p>')
                $("#chat_3").append('<p>'+response.finder11+'</p>')
                $("#chat_1").show();
            }
        })
    });
    $("#chat_3").click(function(){
        $.ajax({
            url:'/post2',
            type:'post',
            data:{
                email_to:$(".myvar2").val(),
                csrfmiddlewaretoken :csrf
            },
            success: function(response){
                $("#chat_3").append('<p>'+response.finder11+'</p>')//2
            }
        })


    });


});