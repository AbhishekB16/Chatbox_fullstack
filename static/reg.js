$(document).ready(function(){
    var csrf=$("input[name=csrfmiddlewaretoken]").val();

    $("#4").click(function(){
        $.ajax({
            url:'/get',
            type:'get',
            data:{
                // button_text:$(this).text()
                button_text:$(this).text()
            },
            
            success: function(response){
                
                $("#4").text(response.seconds)
                $("#seconds").append('<li>'+response.seconds+'</li>')
            }
            
        });
        
    });
    $("#seconds").on('click','li',function(){
        $.ajax({
            url:'/post',
            type:'post',
            data:{
                text: $(this).text(),
                csrfmiddlewaretoken :csrf
            },
            success: function(response){
                $("#right").append('<li>'+response.data+'</li>')
            }
        })
    });

});