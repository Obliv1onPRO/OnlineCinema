import json

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from api import forms, models

from django.contrib import auth
# Create your views here.

def reg_view(request):
    context = {}
    context['form'] = forms.RegistationForm()

    form = forms.RegistationForm(request.POST)
    if form.is_valid():
        username = form.data['username']
        email = form.data['email']
        password = form.data['password']

        if not models.Profile.objects.filter(login=username).exists():
            if not models.Profile.objects.filter(email=email).exists():
                standart_user = models.User.objects.create_user(username=username, password=password, email=email)
                user = models.Profile()
                user.login=username
                user.password=password
                user.email=email
                user.standart_user_id = standart_user.id
                usr = auth.authenticate(username=username, password=password)
                auth.login(request, usr)
                user.save()
                return HttpResponseRedirect('/')
            else:
                context['error'] = "Пользователь с таким email уже существует"
        else:
            context['error'] = "Пользователь с таким ником уже существует"


    return render(request, 'reg.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

def login_view(request):
    context = {}
    context['form'] = forms.LoginForm()

    form = forms.LoginForm(request.POST)
    if form.is_valid():
        username = form.data['username']
        password = form.data['password']

        if models.Profile.objects.filter(login=username).exists():
            if models.Profile.objects.get(login=username).password == password:
                user = models.Profile.objects.get(login=username)
                usr = auth.authenticate(username=username, password=password)
                auth.login(request, usr)
                return HttpResponseRedirect('/profile')
            else:
                context['error'] = "Пароль введён неверно"
        else:
            context['error'] = "Пользователя с таким ником не существует"
    return render(request, 'login.html', context)


@login_required
def create_room(request):
    context = {}

    if request.method == 'POST':
        prs = models.Profile.objects.all()
        # creator = models.Profile.objects.get(login=request.user.username) #FIXME

        data = request.body.decode('utf-8')
        data = json.load(data)

        name = data['name']
        type = request.POST.type
        iframe = request.POST.iframe

        room = models.Room()
        room.name = name
        room.type = type
        room.iframe = iframe
        room.creator = prs
        

    return render(request, 'create_room.html', context)

@login_required
def profile_view(request):
    context = {}
    user = models.Profile.objects.get(pk=request.user.pk)
    context['friends'] = user.friends
    if context['friends'] is None:
        context['friends'] = []

    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def room_view(request):
    context = {}
    return render(request, 'room.html', context)