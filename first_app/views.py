from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'first_app/index.html') # template we wish to you, next file itself, context (link up arguments to index.html)
    # typically tempaltes are separated by apps. 
