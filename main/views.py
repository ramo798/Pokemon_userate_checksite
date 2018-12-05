from django.shortcuts import render, redirect
from .models import pokeinfo
import os, csv
UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'


def index(request):
    return render(request, 'main/index.html', {})
