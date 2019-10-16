from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    list=request.GET['words']
    l=list.split()
    return render(request, 'count.html', {'xyz': len(l)})
