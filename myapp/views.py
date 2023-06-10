from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("index page")


def hello(request, username):
    return HttpResponse("<h2>Hola  %s</h2>" % username)


def about(request):
    return HttpResponse("<h1>about</h1>")


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)


def task(request, id):
    task = get_object_or_404(Task,id=id)
    return HttpResponse("task: %s" % task.title)
