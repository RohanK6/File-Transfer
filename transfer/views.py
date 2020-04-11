from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

from .forms import FileForm, DownloadForm
from .models import File

# Create your views here.
def index(request):
    return render(request, 'transfer/index.html')

def upload(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            context = {}
            userf = form.save(commit = False)
            userf.save()
            context['userf'] = userf
            context['serial'] = userf.serial
            return render(request, 'transfer/success.html', context)
    context = {'form': form}
    return render(request, 'transfer/upload.html', context)

def success(request):
    return render(request, 'transfer/success.html')

def download(request):
    downloadForm = DownloadForm()
    if request.method == 'POST':
        downloadForm = DownloadForm(request.POST)
        if downloadForm.is_valid():
            context = {}
            requestedCode = request.POST['code']
            requestedFile = File.objects.get(serial = requestedCode)
            print(requestedFile.doc.path)


            return render(request, 'transfer/download.html', context)
    context = {'downloadForm': downloadForm}
    return render(request, 'transfer/download.html', context)