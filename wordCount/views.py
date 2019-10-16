from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    y=request.GET['text']
    l=y.split()
    return render(request, 'count.html', {'xyz': len(l)})
