from django.db import models

class Employee(models.Model):
    full_name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    mob_num=models.IntegerField()
    state=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

# Create your models here.
