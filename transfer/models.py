from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

def serial_gen():
    serial_gen = uuid.uuid4().hex.upper()[0:25]
    return serial_gen

class File(models.Model):
    fileName = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    dateUploaded = models.DateTimeField(default = timezone.now)
    doc = models.FileField(null=True)
    serial = models.CharField(max_length = 26, default=serial_gen, unique=True, editable=False,)
    code = models.CharField(max_length = 26, default = "")
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.fileName