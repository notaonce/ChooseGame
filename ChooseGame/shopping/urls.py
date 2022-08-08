from django.urls import path
from shopping import views

app_name = 'shopping'

urlpatterns = [
    path("", views.cash, name='cash'),
]