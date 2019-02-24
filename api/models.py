from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(User):
    standart_user = models.OneToOneField(verbose_name='пользователь', to=User, on_delete=models.CASCADE)
    friends = models.ForeignKey(verbose_name='друзья', to='self', on_delete=models.CASCADE)


class Video(models.Model):
    pass

class Room(models.Model):
    name = models.CharField(verbose_name='имя комнаты', max_length=150)
    iframe = models.CharField(verbose_name='iframe видео')
    creator = models.OneToOneField(verbose_name='создатель', to=Profile, on_delete=models.CASCADE)

    viewers = models.ForeignKey(verbose_name='зрители', to=Profile, on_delete=models.CASCADE)

    class Meta:
        pass
