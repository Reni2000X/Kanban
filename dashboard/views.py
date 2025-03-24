from django.shortcuts import render
from .models import Board 
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render
#from dashboard.models import Board 
import json
from django.http import JsonResponse

def index(request):
    print("User joined the dashboard")
    return render(request, 'dashboard/index.html')

from django.shortcuts import render

def index_new(request):
    print("User joined the dashboard")

    x=Board.objects.all()
    Board_names=[]
    for board_instance in x: 
        
        a=board_instance.name
        Board_names.append(a)
    return render(request, 'dashboard/new_index.html', {'x': x})


def create_new_project(request):
    data = json.loads(request.body)
    print(data)
    new_project = Board(name=data['name'])
    new_project.save()
    print("New project created")

    return JsonResponse({'status': 'success', 'message': 'Project created successfully!'})