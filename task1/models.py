from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.

class User(models.Model):
    user_id = models.AutoField(verbose_name='ID', primary_key=True)
    Name = models.CharField(max_length=50)
    Email_Address = models.EmailField(unique=True)
    DateofBirth = models.DateField()
    Phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name = "User_data"
        verbose_name_plural = "User_data"

    def __str__(self) -> str:
        return str(self.user_id)

# @receiver(pre_save, sender=User)
# def print_email(sender, instance, **kwargs):
#     print(sender.objects.get(user_id=instance.user_id))
#     print(instance)
