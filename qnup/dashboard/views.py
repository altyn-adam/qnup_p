from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'dashboard/index.html', {
        'title': 'Главная страниaца сайта',
        'tasks': tasks
    })

def about(request):
    return render(request, 'dashboard/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не верная!'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'dashboard/create.html', context)