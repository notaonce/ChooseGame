from operator import mod
from statistics import mode
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Paragraph(models.Model):
    para_num = models.CharField(verbose_name='PARA_NUM', max_length=100)
    def __str__(self):
        return f'{self.para_num}'

class Content(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE, related_name='content')
    content = models.TextField()

    def __str__(self):
        return f'{self.paragraph}'

class Choice(models.Model) :
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='choice')
    CHOICES = (
        ('', 'NONE'),        
        ('AT', 'ATTACK'),
        ('DE', 'DEFFENCE'),
    )
    choice = models.CharField(max_length=2, choices=CHOICES, default=CHOICES[0][0])