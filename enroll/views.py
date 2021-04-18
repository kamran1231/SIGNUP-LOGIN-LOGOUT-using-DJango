from django.shortcuts import render,redirect,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully')
            fm = SignupForm()
    else:

        fm = SignupForm()
    return render(request,'signup.html',{'form':fm})



def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            fm = LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                psw = fm.cleaned_data['password']

                user = authenticate(username=uname,password=psw)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfully')
                    return redirect('profile')


        else:
            fm = LoginForm()
        return render(request,'login.html',{'form':fm})

def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('signup')