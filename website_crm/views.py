from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecord
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()
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
        return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

def register_user(request):
        if request.method == "POST":
             form = SignUpForm(request.POST)
             if form.is_valid():
                  form.save()
                  # Authenticate and login
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password1']
                  user = authenticate(username=username,password=password)
                  login(request,user)
                  messages.success(request,"Registration Successfull! Welcome.")
                  return redirect('home')
        else:
            form = SignUpForm()
            return render(request,'register.html',{'form':form})
        return render(request,'register.html',{'form':form})


def customer_record(request,pk):
     if request.user.is_authenticated:
          customer_data = Record.objects.get(id=pk)
          return render(request,'record.html',{'data':customer_data})
     else:
        messages.success(request,"Authentication Failed.")
        return redirect('home')
     
def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_user = Record.objects.get(id=pk)
        if delete_user is not None:
            delete_user.delete()
            messages.success(request,"Deletion Successfull!")
            return redirect('home')
        else:
            messages.error(request,"Error deleting the record")
            return redirect('home')
    else:
            messages.error(request,"Authentication Required")
            return redirect('register.html')
    

def add_record(request):
    form = AddRecord(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
              if form.is_valid():
                   add_record = form.save()
                   messages.success(request,"User Registration Successfull!")
                   return redirect('home')
              else:
                   messages.success(request,"Error submitting the form!")
                   return redirect('home')
        else:
            return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"Authentication Failed!")
        return redirect('home')
     

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecord(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"User Data Updated!")
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,"Authentication Failed!")
        return redirect('home')