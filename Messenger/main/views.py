from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, InputForm
from .models import UserInfo


from django.contrib import messages

from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
def index(request):
    context = {}
    user = request.user
    this_user = UserInfo.objects.get(username = user)
    context['this_user']=this_user
    return render(request, 'main/index.html', context)


@login_required(login_url = 'login')
def about(request):
    return render(request, 'main/about.html')


@login_required(login_url = 'login')
def friends(request):
    return render(request, 'main/friends.html')


@login_required(login_url = 'login')
def users(request):
    return render(request, 'main/users.html')


#flag_registrate = False
def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_form')


    context = {"form":form}
    return render(request, 'main/register.html', context)


def register_form(request):
    context = {}
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            firstname = form.cleaned_data.get("first_name")
            lastname = form.cleaned_data.get("last_name")
            age = form.cleaned_data.get("age")
            job = form.cleaned_data.get("job")
            copy = UserInfo(username = username, age = age, first_name = firstname, last_name = lastname, job = job)
            copy.save()
            context['firstname'] = firstname
            context['lastname'] = lastname
            context['age'] = age
            context['job'] = job
            return redirect('login')
    else:  
        form = InputForm()

    context['form']=form
    return render(request, 'main/reg_form.html', context)


def logoutUser(request):

    logout(request)
    return redirect('login')

def loginPage(request):
    context = {}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Incorrect password or login")
    context = {}
    return render(request, 'main/login.html', context)

def messages(request):
    return render(request, 'main/messages.html')
