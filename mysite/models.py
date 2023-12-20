from django.db import models

# Create your models here.


# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    introduction = models.TextField(max_length=1000) 
    company = models.CharField(max_length=100, default = 'n/a')
    website = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    video = models.CharField(max_length=100)
    counter = models.PositiveIntegerField(default=0)
    def __stt__(self):
        return self.name

# class Video(models.Model):
#     name = models.CharField(max_length=100)
#     link = models.CharField(max_length=100)

# class Photo(models.Model):
#     name = models.CharField(max_length=100)
#     link = models.CharField(max_length=100)


