from django.db import models

import datetime

class Option:
	solution=(
		("ok","Ok"),("return","Return")

		)
	status=(('completed','Completed'),('ongoing','Ongoing'),('waiting','Waiting'),('dispatched','Dispatched'))
	laptop=(
		('dell','Dell'),('hp','HP'),('acer','Acer'),('toshiba','Toshiba'),('asus','ASUS'),('gigabyte','Giga Byte'),('fujitsu','Fujitsu'),('mac','Macbook'),('samsung','Samsung'),('emachine','emachine')
		,('other','Other'))
	desktop=(
		('motherboard','Mother Board'),('cpu','Full CPU'),('printer','Printer'),('smps','SMPS'),('other','Other')
		)
	recovery=(('desktop_hdd','Desktop HDD'),('laptop_hdd','Laptop HDD'),('pendrive','Pen Drive'),('memorycard','Memory Card'))
class Laptop_entry(models.Model):
	
	entry_number=models.CharField(max_length=20,blank=True)
	entry_date=models.CharField(max_length=20,blank=True)
	customer_name=models.CharField(max_length=50)
	contact=models.CharField(max_length=20,blank=True)
	address=models.CharField(max_length=50,blank=True)
	device_name=models.CharField(max_length=50,choices=Option.laptop,blank=True)
	device_detail=models.CharField(max_length=150)
	problem=models.CharField(max_length=150,blank=True)
	solution=models.CharField(max_length=50,choices=Option.solution,blank=True)
	status=models.CharField(max_length=50,choices=Option.status,blank=True)
	remarks=models.CharField(max_length=50,blank=True)
	technician=models.CharField(max_length=50,blank=True)


	def __str__(self):
		return self.customer_name
	
class Desktop_entry(models.Model):
	
	entry_number=models.CharField(max_length=20,blank=True)
	entry_date=models.CharField(max_length=20,blank=True)
	customer_name=models.CharField(max_length=50)
	contact=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	device_name=models.CharField(max_length=50,choices=Option.desktop)
	device_detail=models.CharField(max_length=150)
	problem=models.CharField(max_length=150,blank=True)
	
	solution=models.CharField(max_length=50,choices=Option.solution)
	status=models.CharField(max_length=50,choices=Option.status)
	remarks=models.CharField(max_length=50)
	technician=models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.customer_name


class Recovery(models.Model):
	
	entry_number=models.CharField(max_length=20,blank=True)
	entry_date=models.CharField(max_length=20,blank=True)
	customer_name=models.CharField(max_length=50)
	contact=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	device_name=models.CharField(max_length=50,choices=Option.recovery)
	device_detail=models.CharField(max_length=150)
	problem=models.CharField(max_length=150,blank=True)
	
	solution=models.CharField(max_length=50,choices=Option.solution)
	status=models.CharField(max_length=50,choices=Option.status)
	remarks=models.CharField(max_length=50)
	technician=models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.customer_name

	
