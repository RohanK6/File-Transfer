from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .forms import FileForm
from .models import File

# Create your views here.
def index(request):
    return render(request, 'transfer/index.html')

def upload(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            userf = form.save(commit = False)
            userf.save()
            #print(userf.serial)
            return render(request, 'transfer/upload.html', {'userf': userf})

    context = {'form': form}
    return render(request, 'transfer/upload.html', context)

def download(request):
    return render(request, 'transfer/download.html')