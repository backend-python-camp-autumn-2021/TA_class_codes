from django.urls import path
from .views import _login,logout,change_pass,signup
urlpatterns = [
    path("login/",_login,name="login"),
]
