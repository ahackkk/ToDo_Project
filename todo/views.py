from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Функция для отображения списка задач
def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_title = request.POST.get('task_title')
        if task_title:
            Task.objects.create(title=task_title)
        return redirect('index')
    return render(request, 'todo/index.html', {'tasks': tasks})

# Функция для изменения статуса задачи
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')
