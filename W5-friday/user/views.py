from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm,PasswordChangeForm

def login(request):
    return render(request , "base.html")
    # raise NotImplementedError("Implement Login")
def signup(request):
    raise NotImplementedError("Implement Singup Function")
def logout(request):
    raise NotImplementedError("Implement Logout Function")
def change_pass(request):
    raise NotImplementedError("Implement Change Password Function")
