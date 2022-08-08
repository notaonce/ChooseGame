from turtle import up, update
import re
from django.shortcuts import render, redirect
from shopping.models import UserCash
from django.contrib import messages
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def cash(request) :
    if request.method == 'POST' :
        user = UserCash.objects.get(user=request.user)
        userWallet = user.cash
        UserCash.objects.filter(user=request.user).update(
            cash = userWallet + 10
        )
        messages.success(request, "10캐쉬를 획득하였습니다.")
        return redirect('game:home')
    return render(request, 'cash/cash.html')