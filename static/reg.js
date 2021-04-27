$(document).ready(function(){
    $(".btn").click(function(){
        $.ajax({
            url:'/get',
            type:'get',
            data:{
                // button_text:$(this).text()
                button_text:$(this).text()
            },
            
            success: function(response){
                
                $(".btn").text(response.seconds)
            }
            
        });
        
    });

});