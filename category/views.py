from django.shortcuts import render, redirect, get_object_or_404
from checkmateapp.models import Mate
from checkmateapp.forms import mateForm

def main(request):
    posts = Mate.objects.all()
    return render(request,'main.html',{'posts' : posts})

def travel(request):
    posts = Mate.objects.all()
    return render(request,'travel.html',{'posts' : posts})

def camping(request):
    posts = Mate.objects.all()
    return render(request,'camping.html',{'posts' : posts})

def exercise(request):
    posts = Mate.objects.all()
    return render(request,'exercise.html',{'posts' : posts})

def study(request):
    posts = Mate.objects.all()
    return render(request,'study.html',{'posts' : posts})

def cultural(request):
    posts = Mate.objects.all()
    return render(request,'cultural.html',{'posts' : posts})

def explanation(request):
    return render(request, 'explanation.html')