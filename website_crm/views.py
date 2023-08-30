from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST['username']
        passwd = request.POST['passw']
        # Authenticating User
        user = authenticate(request,username=username,password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in successfully!")
            return redirect('home')
        else:
            messages.error(request,"Invalid login! Username or password is incorrect.")
            return redirect('home')
    else:
        return render(request,'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

def register_user(request):
        return render(request,'register.html',{})