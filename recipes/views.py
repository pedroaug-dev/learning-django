from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('project home')

def about(request):
    return HttpResponse('project about')

def contact(request):
    return HttpResponse('project contact')