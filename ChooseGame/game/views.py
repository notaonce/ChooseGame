import re
from django.shortcuts import render, redirect
from game.models import Storyboard, UserStatus
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

def home(request):
    if request.user.is_authenticated :
        userstatus = UserStatus.objects.get(user=request.user)
        return render(request, 'game/home.html', {'userstatus':userstatus})
    return render(request, 'game/home.html')



def signup(request):
    if request.method == 'POST':
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) > 0):
            error = '이미 존재하는 아이디입니다.'
            return render(request, 'registration/signup.html', {'error': error})
        else:
            new_user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
            new_userStatic = UserStatus.objects.create(
                user = new_user
            )
        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('game:home')
    return render(request, 'registration/signup.html')


def login(request):
    if request.method == 'POST' :
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect(request.GET.get('next', '/'))
    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('game:home')


@login_required(login_url='/login')
def game(request, storyboardname) :
    storyboard = Storyboard.objects.get(storyboard_name=storyboardname)
    localstoryboardbrave = storyboard.brave
    localstoryboardwisdom = storyboard.wisdom
    localdamage = storyboard.damage
    savepoint = storyboard.storyboard_name

    user = request.user
    originaluserstatus = UserStatus.objects.get(user=user)
    localbrave = originaluserstatus.brave
    localwisdom = originaluserstatus.wisdom
    localhp=originaluserstatus.hp
    usersavepoint = originaluserstatus.savepoint

    if usersavepoint != storyboardname :
        userstatuscalculate = UserStatus.objects.filter(user=user).update(
            brave = localbrave+localstoryboardbrave,
            wisdom = localwisdom+localstoryboardwisdom,
            hp = localhp-localdamage,
            savepoint=savepoint
        )

    resultUserStatus = UserStatus.objects.get(user=user)
    resulthp = resultUserStatus.hp
    if resulthp <= 0:
        return redirect('game:result')
    return render(request, "game/game.html", {"storyboard" : storyboard, "userstatus" : resultUserStatus})

@login_required(login_url='/login')
def result(request) :
    UserStatus.objects.filter(user=request.user).update(
        hp=5,
        savepoint='0',
        brave=0,
        wisdom=0,
    )
    return render(request, 'game/result.html')

