
from asyncio.windows_events import NULL
from sre_constants import BRANCH
from django.db import models

# Create your models here.
# class Bank(models.Model):
    
#     Name=models.CharField( max_length=100,verbose_name="name")
#     DOB=models.DateField()
#     Age=models.IntegerField()
#     Gender=models.CharField( max_length=100)
#     email=models.EmailField()

#     address=models.CharField(max_length=120)
#     District=models.CharField(max_length=100)
#     Branch=models.CharField(max_length=120)
#     AccountType=models.CharField(max_length=120)
#     materials=models.CharField(max_length=100)


# class Student(models.Model):
#     name=models.CharField( max_length=100,verbose_name="Student_name")
#     age=models.IntegerField()
#     phone=models.CharField(max_length=12)
#     email=models.EmailField()
#     address=models.CharField(max_length=120,default=NULL)
DISTRICT_CHOICES = (
    ('Kottayam','Kottayam'),
    ('Ernakulam', 'Ernakulam'),
    ('Kollam','Kollam'),
    ('Kozhikodu','Kozhikodu'),
    ('Alapuzha','Alapuzha'),
)
Branch_CHOICES = (
    ('Kottayam','Kottayam'),
    ('Aluva', 'Aluva'),
    ('Kollam','Kollam'),
    ('Kozhikodu','Kozhikodu'),
    ('Alapuzha','Alapuzha'),
)
Account_CHOICES = (
    ('Saving','Saving'),
    ('Current', 'Current'),
    ('Business','Business'),
)
material_CHOICES = (
    ('creditcard','creditcard'),
    ('debitcard', 'debitcard'),
    ('chequebook','chequebook'),
)
class Student(models.Model):
    name=models.CharField( max_length=100,verbose_name="Student_name")
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    address=models.CharField(max_length=120,default=NULL)
    district=models.CharField(max_length=30, choices=DISTRICT_CHOICES, default='Kottayam')
    Branch=models.CharField(max_length=50, choices=Branch_CHOICES, default='Kottayam')
    Accounttype=models.CharField(max_length=50, choices=Account_CHOICES, default='Saving')
    materials=models.CharField(max_length=50, choices=material_CHOICES, default='Saving')

