from django.db import models

# Create your models here.

class Student(models.Model):
    #we can directly write the normal functions 
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    semail=models.EmailField()
