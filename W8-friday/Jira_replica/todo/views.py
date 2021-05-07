from django.shortcuts import render,redirect
from .models import Todo 
from .forms import TodoForm
from django.views.decorators.http import require_POST
from django.views.generic import ListView
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect





class UserPermissionList(ListView):
    model = Permission
    template_name = 'user-perm.html'






def signup_view(request):
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'registration/signup.html', {'form': form})

def index(request):
    todo_list = Todo.objects.order_by("id")
    form = TodoForm()
    context = {"todo_list" : todo_list, 'form' : form}
    return render(request,'index.html',context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    print(request.POST['text'])

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()


    return redirect('index')

def completeTodo(request,todo_id):
        todo = Todo.objects.get(pk=todo_id)
        todo.complete = True
        todo.save()
 
        return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()
 
    return redirect('index')