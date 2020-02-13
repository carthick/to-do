from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages

# Create your views here.

def todolist(request):
    if request.method=='POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Task has beeen created'))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

def contact(request):
    context = {
        "contact_text":"Redirect to Google maps and type Kailasa you will find me.",
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        "about_text":"I am god ",
    }
    return render(request, 'about.html', context)

def delete_task(request, item_id):
    task = TaskList.objects.get(pk=item_id)
    task.delete()
    return redirect('todolist')


def edit_task(request, item_id):
    if request.method =='POST':
        instance = get_object_or_404(TaskList, id=item_id)
        task = TaskList.objects.get(pk=item_id)
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        messages.success(request,('Task has beeen updated'))
        return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=item_id)
        return render(request, 'edit.html', {'task':task})

def update_status(request, item_id, status_flag):
    task = TaskList.objects.get(pk=item_id)
    task.done = status_flag
    task.save()
    return redirect('todolist')