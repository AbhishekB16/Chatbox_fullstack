from django.db import models

class User(models.Model):
    name=models.CharField(max_length=145)
    email=models.CharField(max_length=145)
    pswd=models.CharField(max_length=145)
    date=models.DateField()
    def __str__(self):
        return self.name
    

# Create your models here.
