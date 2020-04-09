from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Task
from django.http import HttpResponseRedirect


def homepage(request):
    current_tasks = Task.objects.all().order_by("-pub_date")
    return render(request, 'coreApp/home.html', {'data': current_tasks})


@csrf_exempt
def addTask(request):
    current_date = timezone.now()
    current_title = request.POST["title"]
    current_body = request.POST["body"]
    Task.objects.create(title=current_title,
                        body=current_body, pub_date=current_date)
    return HttpResponseRedirect("/")


@csrf_exempt
def deleteTask(request, task_id):
    get_object_or_404(Task, pk=task_id).delete()
    return HttpResponseRedirect("/")
