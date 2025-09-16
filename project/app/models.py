from django.db import models
# from .models import Stusent


# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField()
    stu_contact = models.IntegerField()


