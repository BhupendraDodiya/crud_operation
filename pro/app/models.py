from django.db import models

# Create your models here.
class Emp(models.Model):
    Name = models.CharField(max_length=100)
    Contact = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    DOB = models.DateField()