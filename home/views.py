from django.shortcuts import render,HttpResponse
from django.contrib import messages
from home.models import User
from django.views.generic import View
from django.http import JsonResponse
from time import time
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
            return render(request,'chatpage.html')
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
        print("------------xxxx2-----------")
        card_text=request.POST.get('text')
        print("-->"+card_text)
        result= f"I've got : {card_text}"
        return JsonResponse({'data':result},status=200)