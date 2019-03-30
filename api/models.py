from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    standart_user_id = models.IntegerField(verbose_name='id', null=False, default=0)

    login = models.CharField(verbose_name='логин', max_length=50, null=False, default='')
    password = models.CharField(verbose_name='пароль', max_length=100, null=False, default='')
    email = models.EmailField(verbose_name='почта', null=False, default='')
    friends = models.ForeignKey(verbose_name='друзья', to='self', null=True, on_delete=models.CASCADE)


class Video(models.Model):
    pass

class Room(models.Model):
    name = models.CharField(verbose_name='имя комнаты', max_length=150)
    type = models.BooleanField(verbose_name='тип')
    iframe = models.CharField(verbose_name='iframe видео', max_length=2000)
    creator = models.OneToOneField(verbose_name='создатель', to=Profile, on_delete=models.CASCADE)

    viewers = models.ForeignKey(verbose_name='зрители', related_name='viewers', to=Profile, on_delete=models.CASCADE)

    class Meta:
        pass
