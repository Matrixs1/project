from email import message
from tkinter import CASCADE
from django.db import models

# Create your models here.
class department(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    photos = models.ImageField(upload_to="photos")

    def __str__(self):
        return self.name

class doctor(models.Model):
    department_id = models.ForeignKey(department,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    discription = models.TextField()
    photos = models.ImageField(upload_to="photos")
    twitter = models.TextField(null=True,blank=True)
    facebook = models.TextField(null=True,blank=True)
    instagram = models.TextField(null=True,blank=True)
    linkedin = models.TextField(null=True,blank=True)  
    
    class Meta:
        ordering =['name',]

    def __str__(self):
        return self.name  



class contact1(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
        return self.name  