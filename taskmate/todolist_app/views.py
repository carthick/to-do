from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        "index_text":"Welcomen to To Do Application",
    }
    return render(request, 'index1.html', context)

@login_required
def todolist(request):
    if request.method=='POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,('Task has beeen created'))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks':all_tasks})

@login_required
def contact(request):
    context = {
        "contact_text":"Redirect to Google maps and type Kailasa you will find me.",
    }
    return render(request, 'contact.html', context)

def about(request):
    context = {
        "about_text":"I AM GOD ",
    }
    return render(request, 'about.html', context)

@login_required
def delete_task(request, item_id):
    task = TaskList.objects.get(pk=item_id)
    task.delete()
    return redirect('todolist')

@login_required
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
@login_required
def update_status(request, item_id, status_flag):
    task = TaskList.objects.get(pk=item_id)
    task.done = status_flag
    task.save()
    return redirect('todolist')