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
    
    $("#chat_main_right").hide();
    $("#msg31").hide();
    $("#main1").hide();
    $("#6").on('click',function(){
        $("#btn_6").hide();
        $("#msg31").show();
        $("#main1").show();
        var intervalId = window.setInterval(function(){
            $.ajax({
                url:'/valid',
                type:'post',
                data:{
                    email_to:$(".myvar2").val(),
                    csrfmiddlewaretoken :csrf
                },
               
                success: function(response){
                    if((response.msg_gate)){
                    
                var myvar = '<div class="chat chat-left">'+
                '            <div class="chat-body" >'+
                '            <div class="chat-content" name="pra911" >'+
                '            </div>'+
                '         '+
                '          </div>'+
                '        </div>';    
                    $("#chat_appender").append(myvar)//2
                    $('[name="pra911"]').last().append('<p>'+response.finder11+'</p>')
                    }
            }
            })
    
        }, 1000);

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
                
            var myvar = '<div class="chat" id="chat_main_right">'+
            '          <div class="chat-avatar">'+
            '            <a class="avatar avatar-online" data-toggle="tooltip" href="#" data-placement="right" title="" data-original-title="June Lane">'+
            '              <i></i>'+
            '            </a>'+
            '          </div>'+
            '          <div class="chat-body" >'+
            '            <div class="chat-content" name="pra100">'+
            '              <!-- heeelo'+
            '              <p>'+
            '                Good morning, sir.'+
            '                <br>What can I do for you?'+
            '              </p> -->'+
            '              <!-- <time class="chat-time" datetime="2015-07-01T11:37">11:37:08 am</time> -->'+
            '            </div>'+
            '          </div>'+
            '        </div>';
                



                $("#chat_appender").append(myvar)
                $('[name="pra100"]').last().append('<p>'+response.msg11+'</p>')
                // $("#chat_3").append('<p>'+response.finder11+'</p>')
                $("#chat_main_right").show();
            }
        })
    });
    
    


});