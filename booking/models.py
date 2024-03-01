from django.utils import timezone
from django.db import models

# Create your models here.
class patient(models.Model):
    full_name = models.CharField(max_length= 65)
    number = models.IntegerField()
    description = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.full_name
         


