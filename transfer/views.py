from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from django.contrib import messages

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
            context['uploaded'] = True

            return render(request, 'transfer/upload.html', context)
    context = {}
    context['form'] = form 
    context['uploaded'] = False
    return render(request, 'transfer/upload.html', context)

def download(request):
    downloadForm = DownloadForm()
    if request.method == 'POST':
        downloadForm = DownloadForm(request.POST)
        if downloadForm.is_valid():
            context = {}

            requestedCode = request.POST['code'].strip()
            requestedFile = File.objects.get(serial = requestedCode)
            requestedFileURL = requestedFile.doc.url

            context['file_url'] = requestedFileURL
            context['submitted'] = True

            return render(request, 'transfer/download.html', context)
    context = {}
    context['downloadForm'] = downloadForm
    context['submitted'] = False
    return render(request, 'transfer/download.html', context)