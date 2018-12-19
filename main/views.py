from django.shortcuts import render, redirect
from .models import pokeinfo
import os, csv
UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


def index(request):

    info = pokeinfo.objects.all()
    d = {
        'info': info,
        
    }
    return render(request, 'main/ranking.html', d)
