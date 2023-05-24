from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
def base(request):
    pass
def home(request):
    return render(request, "home.html")

def Registration(request):
    if request.method=="POST":
        First_Name = request.POST["first_name"]
        Last_Name = request.POST["last_name"]
        User_Name = request.POST["user_name"]
        Email_Address = request.POST["email"]
        password = request.POST["password"]
        Confirm_Password = request.POST["c_password"]
        if password==Confirm_Password:
            if User.objects.filter(username=User_Name).exists():
                return redirect(Registration)
            elif User.objects.filter(email=Email_Address).exists():
                return redirect(Registration)
            else:
                user=User.objects.create_user(
                    first_name=First_Name , last_name=Last_Name , username=User_Name , email=Email_Address , password=password)
                user.set_password(password)
                user.save()
                return redirect(Login)

    return render(request, "Auth/sign-up.html")

def Login(request):
    if request.method=="POST":
        user_name=request.POST["username"]
        passw=request.POST["password"]
        user=auth.authenticate(username=user_name, password=passw)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            return redirect(Registration)
    return render(request, "Auth/login.html")

def LogOut(request):
    auth.logout(request)
    return redirect(Login)

def Cv_View(request):
    return render(request, "Auth/Cv_View.html")

def UserProfile(request):
    user1= Profile.objects.get(user=request.user)
    # context = (
    #     'user1':user1
    # )

    return render(request, "Auth/New_Profile.html", locals())