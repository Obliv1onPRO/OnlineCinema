from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    standart_user_id = models.IntegerField(verbose_name='id', primary_key=True, null=False, default=-1)

    login = models.CharField(verbose_name='логин', max_length=50, null=False, default='')
    password = models.CharField(verbose_name='пароль', max_length=100, null=False, default='')
    email = models.EmailField(verbose_name='почта', null=False, default='')
    friends = models.ManyToManyField(verbose_name='друзья', to='self', null=True,)

    current_room_id = models.IntegerField(verbose_name='текущая комната', null=True, default=-1)


class Video(models.Model):
    pass

class Room(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)

    name = models.CharField(verbose_name='имя комнаты', max_length=150)
    type = models.BooleanField(verbose_name='тип')
    iframe = models.CharField(verbose_name='iframe видео', max_length=2000)
    creator = models.OneToOneField(verbose_name='создатель', to=Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='дата создания')
    duration = models.IntegerField(verbose_name='продолжительность')

    viewers = models.ManyToManyField(verbose_name='зрители', related_name='viewers', to=Profile)


    class Meta:
        pass
