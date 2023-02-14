from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from webapp.models import Task


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    print(request.POST)
    task_data = {
        'title': request.POST.get('title'),
        'status': request.POST.get('status', 'new'),
        'date': request.POST.get('date', None)
    }
    task = Task.objects.create(**task_data)
    return redirect(f'/')

def detail_view(request):
    task_pk = request.GET.get('pk')
    task = Task.objects.get(pk=task_pk)
    context = {'tasks': task}
    return render(request, context=context)