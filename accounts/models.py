from datetime import datetime
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from pages.models import *

# Create your models here.


class appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date = models.TimeField(default=datetime.now())
    messages = models.TextField()
    department_name = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name