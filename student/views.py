from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as L
# Create your views here.
def index(request):
    return HttpResponse("hello")

def login(request):
    return render(request,'login.html')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    print(username,password)

    user = authenticate(username=username,password=password)
    print(user)
    L(request,user)
    return redirect('/home')

@login_required(login_url='/login/')
def home(request):
    return HttpResponse('hello home page')