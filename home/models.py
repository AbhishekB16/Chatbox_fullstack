from django.db import models
choice=((1,'Male'),(0,'Female'))
class User(models.Model):
    name=models.CharField(max_length=145)
    email=models.CharField(max_length=145)
    pswd=models.CharField(max_length=145)
    gender=models.IntegerField(choices=choice,default=1)
    date=models.DateField()
    def __str__(self):
        return self.name
class message(models.Model):
    frm=models.CharField(max_length=145)
    to=models.CharField(max_length=145)
    msg=models.CharField(max_length=1405)
    def __str__(self):
        return self.frm
# Create your models here.
