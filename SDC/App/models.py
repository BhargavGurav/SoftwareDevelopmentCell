from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    Student = models.OneToOneField(User, on_delete=models.CASCADE)
    Mobile = models.CharField(max_length=10)
    PRN = models.BigIntegerField()
    Branch = models.CharField(max_length=35)
    Year = models.CharField(max_length=3)

    def __str__(self):
        return (self.Student.first_name +' '+ self.Student.last_name)

class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Message = models.TextField()

    def __str__(self):
        return self.Email

class CodingProfile(models.Model):
    Coder = models.OneToOneField(User,  on_delete=models.CASCADE)
    Leetcode = models.URLField(max_length=150)
    Github = models.URLField(max_length=150)
    Hackerrank = models.URLField(max_length=150)
    Linkedin = models.URLField(max_length=200, null=True)

    def __str__(self):
        return (self.Coder.first_name +' '+ self.Coder.last_name)
    
    
    

