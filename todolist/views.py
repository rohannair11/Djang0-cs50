from django.shortcuts import render

# Create your views here.
tasks = ["foo", "bar", "fiz"]
def index(request):
    return render(request, "todolist/index.html",{
        "tasks": tasks
    })

def add(request):
    return render(request, "todolist/add.html")