from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages
from multiprocessing import context
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def base(request):
    return render(request, 'base.html')

def cash_bank(request):
    return render(request, 'cash_bank.html')

def cash(request):
    return render(request, 'cash.html')

# Create your views here.
