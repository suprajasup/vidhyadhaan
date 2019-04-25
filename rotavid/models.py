from django.db import models

# Create your models here.

class Student(models.Model):
    Ano=models.CharField(max_length=100)
    Sname = models.CharField(max_length=250)
    Sphoto=models.ImageField(upload_to="all_covers/")
    Fname = models.CharField(max_length = 250)
    Fphoto=models.ImageField(upload_to="all_covers/")
    Mname = models.CharField(max_length = 250)
    Mphoto=models.ImageField(upload_to="all_covers/")
    School = models.CharField(max_length = 500)
    Grade = models.CharField(max_length=100)
    PYmarks=models.ImageField(upload_to="all_covers/")
    PPYmarks=models.ImageField(upload_to="all_covers/")
    Marks=models.CharField(max_length=100)
    Incomecert=models.ImageField(upload_to="all_covers/")
    Foccup=models.CharField(max_length=100)
    Moccup=models.CharField(max_length=100)
    Sfee=models.CharField(max_length=100)
    Scholar=models.CharField(max_length=100)

    def __str__(self):
        return self.Sname