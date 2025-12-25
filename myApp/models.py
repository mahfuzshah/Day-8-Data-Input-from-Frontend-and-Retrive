from django.db import models

class StudentModel(models.Model):
    Name=models.CharField(max_length=100, null=True)
    Email=models.EmailField(max_length=50, null=True)
    Contact=models.CharField(max_length=20, null=True)
    Age=models.IntegerField(null=True)
    City=models.CharField(max_length=50, null=True)

class TeacherModel(models.Model):
    Name=models.CharField(max_length=100, null=True)
    Email=models.EmailField(max_length=100, null=True)
    Subject=models.CharField(max_length=100, null=True)
    Department=models.CharField(max_length=100, null=True)
    City=models.CharField(max_length=50, null=True)

class ProductModel(models.Model):
    Name=models.CharField(max_length=100, null=True)
    Price=models.IntegerField(null=True)
    Category=models.CharField(null=True)
    Department=models.CharField(max_length=100, null=True)
    City=models.CharField(max_length=50, null=True)
