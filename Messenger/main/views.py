from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, InputForm, SearchForm
from .models import UserInfo
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

@login_required(login_url = 'login')
def index(request):
    context = {}
    user = request.user
    this_user = UserInfo.objects.get(username=user)
    context['this_user'] = this_user
    flag = 0
    if r.get(this_user.username):
        room = str(r.get(this_user.username))
        length = len(room)
        room = room[2:length-1]
        print("You got invitation to room : ", room)
        flag = 1
        context['room'] = room
        r.delete(user.username)
    context['flag'] = flag
    return render(request, 'main/index.html', context)

@login_required(login_url = 'login')
def about(request):
    return render(request, 'main/about.html')


@login_required(login_url = 'login')
def friends(request):
    context = {}
    user = request.user
    this_user = UserInfo.objects.get(username=user)
    friends = this_user.friends
    print('My friends: ', friends.split(' '))
    friends_array = friends.split(' ')
    i = 1
    friends_objects_array = []
    invite = request.GET.get('invite-button', '')
    room_name = request.GET.get('chat_room_name','')
    if invite and room_name:
        print('Invite button pushed : ', invite)
        print('Chat room name: ', str(room_name))
        r.set(invite, room_name)
    while (i < len(friends_array)):
        friends_objects_array.append(UserInfo.objects.get(username = friends_array[i]))
        i = i + 1
    context['friends'] = friends_objects_array
    context['this_user'] = this_user
    return render(request, 'main/friends.html', context)


@login_required(login_url = 'login')
def users(request):
    context = {}
    user = request.user
    this_user = UserInfo.objects.get(username=user)
    context["this_user"] = this_user
    inp_value = request.GET.get('results', '')
    print("Input value: ", inp_value)
    inp_value = str(inp_value)
    objects = UserInfo.objects.all()
    flag = 0
    for i in range(len(objects)):
        if (inp_value == objects[i].username):
            context['result_user'] = objects[i]
            flag = 1
            break
    name = request.GET.get('add-friend-btn','')
    if name:
        if not (name in this_user.friends):
            new_name = str(this_user.friends) + name
            print("You already this friend")
            this_user.friends = new_name
            this_user.save()
        else : print("You already have this friend")
    return render(request, 'main/users.html', context)


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


