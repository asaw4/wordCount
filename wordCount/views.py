from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    y=request.GET['text']
    l=y.split()

    dict={}
    for word in l:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    print(dict)
    return render(request, 'count.html' , { 'text': y , 'xyz': len(l) , 'dic': dict})

def about(request):
    return render(request,'about.html')
