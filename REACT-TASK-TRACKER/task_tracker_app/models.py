from django.db import models

# Create your models here.
class Tasks(models.Model):
    text = models.CharField(max_length=250)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    reminder = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tasks"
