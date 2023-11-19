from django.db import models
from PATIENT.models import *
from .models import *
from COMMON_APP.models import *
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length=40)
	phone = models.IntegerField(max_length=10,default="",unique=True)
	email = models.EmailField(max_length=50,unique=True)
	gender = models.CharField(max_length=30)
	address = models.CharField(max_length=200)
	age = models.IntegerField(default= 0)
	blood = models.CharField(max_length=10)
	username = models.OneToOneField(User,on_delete = models.CASCADE)
	status = models.BooleanField(default = 0)
	department = models.CharField(max_length=30 , default = "")
	attendance = models.IntegerField(default = 0)
	salary = models.IntegerField(default = 10000)
	
	def __str__(self):
		return self.name

	
# Prescription Model

class Prescription2(models.Model):
	prescription = models.CharField(max_length=200)
	symptoms = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient,on_delete = models.CASCADE,unique = False)
	doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE,unique = False)
	appointment = models.ForeignKey('COMMON_APP.Appointment',on_delete = models.CASCADE,unique = False)
	prescripted_date = models.DateField(auto_now = True) 
	outstanding = models.IntegerField(default = 0)
	paid = models.IntegerField(default = 0)
	total = models.IntegerField(default = 0)

	def __str__(self):
		return self.prescription


