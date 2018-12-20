from django.shortcuts import render, redirect
from .models import pokeinfo
import os, csv
UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


def index(request):

    info = pokeinfo.objects.filter(no__lt= 41)

    graf = pokeinfo.objects.filter(no__lt= 12)
    d = {
        'info': info,
        'graf': graf,
    }
    return render(request, 'main/ranking.html', d)
