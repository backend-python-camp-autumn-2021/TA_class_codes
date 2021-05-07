from django.shortcuts import render
from django.contrib.auth.forms import  UserCreationForm,AuthenticationForm,PasswordChangeForm

# from .models import  User

from django.contrib.auth import get_user_model
User = get_user_model()

class SignUpForm(UserCreationForm):

   class Meta:
      model = User  
      fields = ('username', 'password1', 'password2')

def _login(request):
    return render(request , "base.html")
    # raise NotImplementedError("Implement Login")
def signup(request):
    raise NotImplementedError("Implement Singup Function")
def logout(request):
    raise NotImplementedError("Implement Logout Function")
def change_pass(request):
    raise NotImplementedError("Implement Change Password Function")
