from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from api import forms, models

from django.contrib import auth
# Create your views here.

def reg(request):
    context = {}
    context['form'] = forms.RegistationForm()

    form = forms.RegistationForm(request.POST)
    if form.is_valid():
        username = form.data['username']
        email = form.data['email']
        password = form.data['password']

        if not models.User.objects.filter(username=username).exists():
            if not models.User.objects.filter(email=email).exists():
                user = models.User.objects.create_user(username=username, password=password, email=email)
                auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                context['error'] = "Пользователь с таким email уже существует"
        else:
            context['error'] = "Пользователь с таким ником уже существует"


    return render(request, 'reg.html', context)

def index(request):
    context = {}
    return render(request, 'index.html', context)

def login(request):
    context = {}
    context['form'] = forms.LoginForm()

    form = forms.LoginForm(request.POST)
    if form.is_valid():
        username = form.data['username']
        password = form.data['password']

        if models.User.objects.filter(username=username).exists():
            if models.User.objects.get(username=username).check_password(password):
                user = models.User.objects.get(username=username)
                auth.authenticate(username=username, password=password)
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                context['error'] = "Пароль введён неверно"
        else:
            context['error'] = "Пользователя с таким ником не существует"
    return render(request, 'login.html', context)


def create_room(request):
    context = {}
    return render(request, 'create_room.html', context)


def profile(request):
    context = {}
    return render(request, 'profile.html', context)