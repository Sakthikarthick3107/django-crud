from django.db import models

# Create your models here.

class ToDo(models.Model):
    sno = models.AutoField(primary_key= True)
    task = models.CharField(max_length= 200)
    completed = models.BooleanField(default = False)
    
    
