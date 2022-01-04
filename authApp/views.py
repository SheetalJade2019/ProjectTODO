from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Todo
#from collections.forms import ContactForm
# Create your views here.
# comment added

def home(request):
    return render(request,"authApp/home.html")

def about(request):
    return render(request,"authApp/about.html")

def contactus(request):
    return render(request,"authApp/contactus.html")

def register(request):
    f = UserCreationForm()
    #print(request.method)
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        #print("testing")
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect('/todohome/')
    else:
        f = UserCreationForm()
    return render(request,"authApp/register.html", {'form': f})

def todohome(request):
    if request.user.is_authenticated:
        todoitem = Todo.objects.all()
        print(todoitem)
        return render(request,"authApp/todo.html",{'todoitem':todoitem})
    else:
        return HttpResponseRedirect('/login/')

def deleteTodo(request,id):
    #if request.user.is_authenticated:
        todelete = Todo.objects.get(id=id)
        todelete.delete()
        return HttpResponseRedirect('/todohome/')
    #else:
    #    return HttpResponseRedirect('/login/')

def addTodo(request):

    newtodo = request.POST['task']
    print(newtodo)
    newtask = Todo(task=newtodo)
    print(newtask)
    newtask.save()
    return HttpResponseRedirect('/todohome/')

def logout_url(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,"authApp/home.html")

def login_url(request):
    f=AuthenticationForm()
    if request.method == "POST":
        f=AuthenticationForm(request=request, data=request.POST)
        if f.is_valid():
            un = f.cleaned_data['username']
            pw = f.cleaned_data['password']
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/todohome/')
        else:
            f=AuthenticationForm()
    return render(request,"authApp/login.html", {'form': f})
