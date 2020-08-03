from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=120)
    birthdaye = models.DateField(null=True , blank=True)
