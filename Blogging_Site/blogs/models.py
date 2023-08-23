from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    blogtext=models.TextField()
    datetime=models.DateTimeField(default=datetime.now())
    

