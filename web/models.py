from django.db import models
from django.utils.timezone import now

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    ad_num = models.IntegerField()
    department = models.CharField(max_length=150)

class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(default=now)
    author = models.CharField(max_length=100, default=0)
    image = models.ImageField(upload_to='gallery/', default=0)
    fl = models.FileField(upload_to='documents/', default=0)

#CRUD
#obj = Student(name=abc, age=sd, ad_num=cfewd)
#obj.save()

# Student.objects.all()


