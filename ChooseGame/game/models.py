
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

#스토리보드(문단)

class Storyboard(models.Model):
    storyboard_name = models.CharField(verbose_name='STORYBOARD_NAME', max_length=100, default="")
    content = models.TextField()
    choice_attack = models.CharField(max_length=100, default='')
    choice_defence = models.CharField(max_length=100, default='')
    brave = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.storyboard_name}'

class UserStatus(models.Model) :
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='userStatic')
    hp = models.IntegerField(default=5)
    brave = models.IntegerField(default=0)
    wisdom = models.IntegerField(default=0)
    savepoint = models.CharField(default='0', max_length=100)

    def __str__(self):
        return f'{self.user}'
