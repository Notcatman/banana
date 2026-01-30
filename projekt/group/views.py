from django.shortcuts import render, get_object_or_404
from .models import *


def list(request):
    tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
    }

    return render(request, 'base.html', context)

def detail(request, id):
    task = get_object_or_404(Task, id=id)

    context = {
        'task': task,
    }

    return render(request, 'detail.html', context)
