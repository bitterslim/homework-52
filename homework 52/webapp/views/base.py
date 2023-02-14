from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Task


def index_view(request: WSGIRequest):
    task = Task.objects.all()
    context = {
        'task' : task
    }
    return render(request, 'index.html', context=context)