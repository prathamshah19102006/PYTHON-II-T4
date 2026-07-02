from django.db import models

# Create your models here
class Student(models.Model):
    name=models.CharField()
    rollno=models.IntegerField()
    score=models.IntegerField()
    def __str__(self):
        return self.name
class Book(models.Model):
    authname=models.CharField()
    bookname=models.CharField()
    def __str__(self):
        return self.bookname