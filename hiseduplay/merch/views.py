from django.shortcuts import render, redirect
from .models import Merch

# Create your views here.

def merch(request):
    return render(request, 'merch/merch.html')

def quiz(request):
    return render(request, 'merch/quiz.html')