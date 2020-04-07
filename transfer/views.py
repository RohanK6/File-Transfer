from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .models import File

# Create your views here.
def index(request):
    return render(request, 'transfer/index.html')

def upload(request):
    return render(request, 'transfer/upload.html')

def download(request):
    return render(request, 'transfer/download.html')