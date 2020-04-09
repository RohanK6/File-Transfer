from django.db import models
from django.utils import timezone
import uuid
# Create your models here.
class File(models.Model):
    fileName = models.CharField(max_length = 30)
    description = models.CharField(max_length = 100)
    dateUploaded = models.DateTimeField(default = timezone.now)
    doc = models.FileField(null=True)
    serial = models.CharField(max_length = 6, default = uuid.uuid4().hex[:20].upper(), unique = True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.fileName