from django.shortcuts import render
from .models import Job
# Create your views here.
def index(request):
    return render(request, 'jobs/home.html')


def homepage(request):
    jobs = Job.objects.all
    return render(request, 'jobs/homepage.html', {'jobs': jobs})