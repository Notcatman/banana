from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import TaskForm


def list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    context = {
        'tasks': tasks,
        'form': form,
    }

    return render(request, 'base.html', context)


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        
        tasks = Task.objects.all()
        context = {
            'tasks': tasks,
            'form': form,
        }
        return render(request, 'base.html', context)
    return redirect('tasks')
    

    

def detail(request, id):
    task = get_object_or_404(Task, id=id)

    context = {
        'task': task,
    }

    return render(request, 'detail.html', context)

def delete(request, list_id):
    item = Task.objects.get(pk=list_id)
    item.delete()
    return redirect('tasks')

    
def cross(request, list_id):
    item = Task.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('tasks')

def uncross(request, list_id):
    item = Task.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('tasks')