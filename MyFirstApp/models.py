from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Details(models.Model):
    type=models.CharField(max_length=20,default='',null=False)
    name=models.CharField(max_length=30,default='',null=False)

    def __str__(self):
        return self.type + " " + self.name
