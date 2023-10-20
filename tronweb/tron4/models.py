from django.db import models

# Create your models here.


class querydetail(models.Model):
    name = models.CharField(max_length= 255)
    phoneno = models.CharField(max_length=13)
    email = models.CharField(max_length= 255)
    msg = models.CharField(max_length= 255)

class visitcounter(models.Model):
    modelcount = models.IntegerField()
    
