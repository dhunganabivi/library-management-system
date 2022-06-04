from django.db import models


class Book(models.Model):
  b_isbn= models.CharField(max_length=40)
  b_name= models.CharField(max_length=100)
  b_price= models.CharField(max_length=20)
  b_authorname= models.CharField(max_length=100)
  b_image= models.ImageField(upload_to = 'b_image')
  

  def __str__(self):
    return self.b_name

  
class Student(models.Model):
  name=models.CharField(max_length=50)
  age= models.IntegerField()
  contact=models.CharField(max_length=20)

  def __str__(self):
    return self.name

class Staff(models.Model):
  name=models.CharField(max_length=30)
  age=models.IntegerField()
  position=models.CharField(max_length=30)
  def __str__(self):
    return self.name

class Library_details(models.Model):
  b_name=models.CharField(max_length=100)
  student= models.ManyToManyField(Student)

  def __str__(self):
    return self.b_name

 

