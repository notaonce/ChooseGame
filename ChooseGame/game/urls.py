from django.urls import path
from game import views

app_name = 'game'

urlpatterns = [
    path("", views.home, name='home'),
    path("game/", views.game, name='game'),
    path("signup/", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("game/<str:storyboardname>", views.game, name='game'),
    path("result", views.result, name='result'),
]