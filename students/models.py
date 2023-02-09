from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    Student_id = models.AutoField(verbose_name='ID', primary_key=True)
    Name = models.CharField(max_length=20)
    DateofBirth = models.DateField(max_length=10)
    Branch = models.CharField(max_length=10, default='Mech')
    Email_address = models.EmailField(max_length=125, default='company@gmail.com',unique=True)
    Phone_number = models.CharField(max_length=12, default="0000000000")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Students_data"
        verbose_name_plural = "Students_data"

    def __str__(self) -> str:
        return str(self.Student_id)

class Student_info(models.Model):
    Stu_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    Stu_name = models.CharField(max_length=50, blank=True)
    Course = models.CharField(max_length=50, blank=True)
    HOD = models.CharField(max_length=50)
    class_teacher = models.CharField(max_length=50)
    #Course = models.ForeignKey(Student, on_delete=models.CASCADE, related_name=)

    class Meta:
        verbose_name = "Other_info"
        verbose_name_plural = "Other_info"

    def __str__(self):
        return str(self.Stu_id)

    @property
    def name(self):
        return self.Stu_id.Name

@receiver(post_save, sender=ap)
def do_something(sender, instance, **kwargs):
    try:
        obj = Student_info.objects.get(Student_id=instance.Student_id)
        print(obj)
    except sender.DoesNotExist:
        pass