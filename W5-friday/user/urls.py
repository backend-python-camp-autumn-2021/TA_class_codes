from django.urls import path
from .views import login,logout,change_pass,signup
urlpatterns = [
    path("login/",login,name="login"),
]
