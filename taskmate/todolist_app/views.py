from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList

# Create your views here.

def todolist(request):
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