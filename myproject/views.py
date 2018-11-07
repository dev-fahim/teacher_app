""""
Created on Nov 4, 2018

@author: Fahim
"""
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})
