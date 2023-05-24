from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path("Registration/", Registration, name="Registration"),
    path("Login/", Login, name="Login"),
    path("LogOut/", LogOut, name="LogOut"),

    path("Cv_View/", Cv_View, name="Cv_View"),
    path("UserProfile/", UserProfile, name="UserProfile"),

]