from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=15) #first name
    lname = models.CharField(max_length=15) #last name
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.fname + " " + self.lname

class Tutor(models.Model):
    fname = models.CharField(max_length=15) #first name
    lname = models.CharField(max_length=15) #last name
    email = models.EmailField()
    grade = models.CharField(max_length=15)
    lesson = models.CharField(max_length=50, default='Default')

    def __str__(self):
        return self.fname + " " + self.lname