from django.db import models

# Create your models here.
class Contect(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    desc = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.name