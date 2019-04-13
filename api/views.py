import datetime
import json

import django
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View as generic_view

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


@method_decorator(login_required, name='dispatch')
class RoomCreating(generic_view):

    def get(self, request):
        context = {}

        creator = models.Profile.objects.get(login=request.user.username)  # FIXME
        if creator.current_room_id is not None:
            return HttpResponseRedirect('/room/' + str(creator.current_room_id))

        return render(request, 'create_room.html', context)

    def post(self, request):
        creator = models.Profile.objects.get(login=request.user.username)  # FIXME

        data = request.body.decode('utf-8')
        data = json.loads(data)

        name = data['name']
        type = data['type']
        iframe = data['iframe']
        duration = data['duration']

        for r in models.Room.objects.all():
            r.delete()

        room = models.Room()
        room.name = name
        room.type = type
        room.iframe = iframe
        room.creator = creator
        room.duration = duration
        # room.created_at = datetime.datetime.now()
        room.save()
        room.viewers.add(creator)

        creator.current_room_id = room.id
        creator.save()

        return HttpResponse(str(room.id))


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


@login_required
def room_view(request, id):
    context = {}
    return render(request, 'room.html', context)