from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import User,message
from django.views.generic import View
from django.http import JsonResponse
from time import time
from datetime import datetime
# Create your views here.
def signin(request):
    #return HttpResponse("this is check")
    if request.method=="POST":
        email=request.POST.get('email')
        pswd1=request.POST.get('password')
        try:
            temp = User.objects.get(email=email)
        except User.DoesNotExist:
            temp = None
        if temp is None:
            messages.warning(request, 'User Not Found')
            return render(request,'signin.html')

        if temp.pswd==pswd1:
            # messages.success(request, "Success")
            context={
                "emailadd":email,
                "gender":temp.gender,
                "logout":1
            }
            return render(request,'chatpage.html',context)
        else: 
            messages.warning(request, 'In-Valid Credentials')
            # return render(request,'signin.html')
    return render(request,'signin.html')
def register(request):
    return render(request,'register.html')
class AjaxHandlerView(View):
    def get(self,request):
        # request.GET.get('course','')
        text=request.GET.get('button_text')
        # print("------------xxxx-----------")
        if request.is_ajax():
            t=time()
            return JsonResponse({'seconds':t},status=200)

        # return HttpResponse("hey")
        return render(request,'register.html')
    def post(self,request):
        # print("------------xxxx4-----------")
        card_text=request.POST.get('text')
        from_email=request.POST.get('email')
        to_email=request.POST.get('email_to')
        # finder=message.objects.filter(to=from_email)
        # print(finder[0].msg)
        # print(finder[len(finder)-1].msg)
        saver=message(frm=from_email,to=to_email,msg=card_text,date_created=datetime.now())
        saver.save()
        print(from_email+"-->"+to_email)
        # result= f"I've got : {card_text}"
        context={
            "msg11":card_text,
            # 'finder11':finder[len(finder)-1].msg
        }
        return JsonResponse(context,status=200)
    # def post2(self,request):
    #     # print("------------xxxx4-----------")
    #     to_email=request.POST.get('email_to')
    #     finder=message.objects.filter(to=to_email)
    #     print(finder[len(finder)-1].msg)
    #     context={
    #         'finder11':finder[len(finder)-1].msg,
    #         # "finder11":'hellllo11'
    #     }
    #     return JsonResponse(context,status=200)
def validator(request):
    # print("------------xxxx4-----------")
    to_email=request.POST.get('email_to')
    finder=message.objects.filter(frm=to_email).filter(delivered=0).order_by('date_created')
    # print(to_email)
    # print(finder[len(finder)-1].msg)
    msg_text=""
    msg_gate=0
    ln1=len(finder)
    # for i in finder:
    #     print(i.msg)   
    #     print(i.date_created)

    
    # print("length=",ln1)
    if ln1>0:
        msg_gate=1
        kep=finder[0]
        msg_text=kep.msg
        # print("---------->report1=",kep.delivered)
        # print(msg_text)
        kep.delivered=1
        # print("---------->report2=",kep.delivered)
        kep.save(update_fields=['delivered'])
    context={
        'finder11':msg_text,
        'msg_gate':msg_gate,
        # "finder11":'hellllo11'
    }
    return JsonResponse(context,status=200)

