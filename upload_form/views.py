from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.conf import settings
from upload_form.models import FileNameModel
from main.models import pokeinfo
import sys, os, csv

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/files/'

def form(request):
    if request.method != 'POST':
        return render(request, 'upload_form/form.html')

    file = request.FILES['file']
    path = os.path.join(UPLOADE_DIR, file.name)
    destination = open(path, 'wb')

    for chunk in file.chunks():
        destination.write(chunk)

    insert_data = FileNameModel(file_name = file.name)
    insert_data.save()
    #csv処理
    with open(path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            mode = pokeinfo()
            mode.pokename = row[0]
            mode.pokerate = row[1]
            mode.waza1 = row[2]
            mode.waza2 = row[3]
            mode.waza3 = row[4]
            mode.waza4 = row[5]
            mode.waza5 = row[6]
            mode.waza6 = row[7]
            mode.waza7 = row[8]
            mode.waza8 = row[9]
            mode.wazarate1 = row[10]
            mode.wazarate2 = row[11]
            mode.wazarate3 = row[12]
            mode.wazarate4 = row[13]
            mode.wazarate5 = row[14]
            mode.wazarate6 = row[15]
            mode.wazarate7 = row[16]
            mode.wazarate8 = row[17]
            mode.save()


    return redirect('upload_form:complete')

def complete(request):
    return render(request, 'upload_form/complete.html')
