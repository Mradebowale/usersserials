from django.urls import path
from .views import CreateUserView, Homepage       # APP URL

urlpatterns = [
    path("home/", Homepage.as_view(), name="home"),
    path("register/", CreateUserView.as_view(), name="register")
]