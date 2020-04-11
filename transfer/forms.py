from django import forms
from .models import File 

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = [
        'fileName',
        'description',
        'doc'
        ]
class DownloadForm(forms.ModelForm):
    class Meta:
        model = File 
        fields = [ 
        'code'
        ]