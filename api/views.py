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