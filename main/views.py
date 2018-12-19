from django.shortcuts import render, redirect
from .models import pokeinfo
import os, csv
UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


def index(request):
    pokename = pokeinfo.objects.all()
    d = {
        'pokename': pokename,
    }
    return render(request, 'main/ranking.html', d)
