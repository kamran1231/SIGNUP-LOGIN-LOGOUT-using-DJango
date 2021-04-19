from django.shortcuts import render,redirect,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm,LoginForm,ChangePassword,ForgetPassword,EditUserProfileForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

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
        if request.method == 'POST':
            fm = EditUserProfileForm(instance=request.user,data=request.POST)
            if fm.is_valid():
                messages.success(request,'User Details Update Successfully!!')
                fm.save()
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'profile.html',{'name':request.user,'form':fm})
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('signup')


#Change Password With OLD password
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ChangePassword(user=request.user,data=request.POST)
            print(fm)
            if fm.is_valid():
                fm.save()
                #if you want to redirect your homepage
                update_session_auth_hash(request,fm.user)
                messages.success(request,'Password has been changed')
                return redirect('profile')

        else:

            fm = ChangePassword(user=request.user)
        return render(request,'changepsw.html',{'form':fm})
    else:
        return redirect('login')



#Change Password without Old Password

def forget_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ForgetPassword(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, 'Your password has been changed')
                return redirect('profile')
        else:
            fm = ForgetPassword(user=request.user)
        return render(request,'forgetpsw.html',{'form':fm})
    else:
        return redirect('login')




