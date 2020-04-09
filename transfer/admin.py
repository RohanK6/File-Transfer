from django.contrib import admin
from .models import File

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('File Name', {'fields': ['fileName']}),
        ('File Description', {'fields': ['description']}),
        ('Upload Date', {'fields': ['dateUploaded']}),
        ('Serial', {'fields': ['serial']}),
        ('ID', {'fields': ['id']})
    ]

    list_display = ('fileName', 'description', 'dateUploaded', 'serial', 'id')
    list_filter = ['dateUploaded']
    search_fields = ['fileName']

admin.site.register(File, FileAdmin)