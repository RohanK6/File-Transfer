from django.db import models

# Create your models here.
class File(models.Model):
    fileName = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    dateUploaded = models.DateTimeField('Date Uploaded')
