from operator import mod
from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class UserCash(models.Model) :
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='userCash')
    cash = models.IntegerField(default=0)