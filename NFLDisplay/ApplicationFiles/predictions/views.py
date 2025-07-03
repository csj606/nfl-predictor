from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    #TODO
    return render(request, "predictions/home.html")


def teams(request):
    #TODO
    return render(request, "predictions/home.html")


def challenges(request):
    #TODO
    return render(request, "predictions/home.html")


def rankings(request):
    #TODO
    return render(request, "predictions/home.html")


@login_required
def league(request):
    #TODO
    return render(request, "predictions/home.html")
