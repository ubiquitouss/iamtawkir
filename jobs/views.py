from django.shortcuts import render
from .models import job


def home(request):
    jobs = job.objects
    return render(request, 'jobs/home.htm', {'jobs': jobs})
