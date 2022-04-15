from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Hello World!</h1>')

def cafe(request):
    return render(request, 'cafe/index.html')