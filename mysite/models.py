from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Company(models.Model):
    name = models.CharField(max_length=100)
    introdcution = models.TextField(max_length=1000) 
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)

class Video(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

class Photo(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)


