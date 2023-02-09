from django.db import models


# Create your models here.

class Youtube(models.Model):
    Vedio_id = models.AutoField(verbose_name='ID', primary_key=True)
    id = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    title = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Youtube_data"
        verbose_name_plural = "Youtube_data"

    def __str__(self) -> str:
        return str(self.Vedio_id)
