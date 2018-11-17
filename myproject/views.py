""""
Created on Nov 4, 2018

@author: Fahim
"""

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'index.html', {})


def index_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            return HttpResponseRedirect(reverse('login'))
    return render(request, 'authentication/index.html', {})


@login_required
def index_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
