from django.shortcuts import render
from .models import Board 
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render

def index(request):
    print("User joined the dashboard")
    return render(request, 'dashboard/index.html')

def index_new(request):
    print("User joined the dashboard")
    return render(request, 'dashboard/new_index.html')

def create_new_project(request):
    
    new_project = Board(name="test project1")
    new_project.save()
    print("New project created")

    return JsonResponse({'status': 'success', 'message': 'Project created successfully!'})