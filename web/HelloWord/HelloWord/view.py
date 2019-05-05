from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse("Hello world ! ")
    context = {}
    context['hello'] = 'Hello World!'
    return render(request,'hello.html',context)
