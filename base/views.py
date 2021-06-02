from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from base.models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    context_object_name = 'task'
    fields = '__all__'
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    fields = '__all__'
    model = Task
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

