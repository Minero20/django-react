from django.db import models

# Create your models here.
class User(models.Model):
    uuid = models.CharField(max_length=200)
    prefix = models.CharField(max_length=60)
    name = models.CharField(max_length=100)
def __str__(self):
        return self.uuid
