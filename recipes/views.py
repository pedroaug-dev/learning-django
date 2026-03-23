from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html')

def about(request):
    return HttpResponse('project about')

def contact(request):
    return HttpResponse('project contact')