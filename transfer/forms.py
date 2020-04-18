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
        widgets = {
            'fileName': forms.TextInput(attrs={'placeholder': 'File Name'}),
            'description': forms.TextInput(attrs={'placeholder': 'File Description'}),
            'doc': forms.FileInput(attrs={'id': 'real-btn'})
        }
class DownloadForm(forms.ModelForm):
    class Meta:
        model = File 
        fields = [ 
        'code'
        ]
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'File Code'})
        }