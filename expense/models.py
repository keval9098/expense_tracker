from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class spent(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.CASCADE)
    spent_on=models.CharField(max_length=100)
    amount=models.IntegerField(default=0)
    reason=models.CharField(max_length=200)
    date=models.DateTimeField(default=datetime.datetime.now()) 

