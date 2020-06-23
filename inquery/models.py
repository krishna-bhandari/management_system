from django.db import models

class Inquery(models.Model):
	sources=(
		('facebook','Facebook'),('google','Google'),('friend','Friend'),('youtube','Youtube'),('marketing','Marketing/Ads')
		)

	entry_number=models.CharField(max_length=20,blank=True)
	entry_date=models.CharField(max_length=20,blank=True)
	 
	customer_name=models.CharField(max_length=50)
	contact=models.CharField(max_length=20,blank=True)
	address=models.CharField(max_length=50,blank=True)
	# device_name=models.CharField(max_length=50,choices=Option.laptop,blank=True)
	inquery_detail=models.CharField(max_length=1000)
	source=models.CharField(max_length=50,choices=sources,blank=True)
	
	remarks=models.CharField(max_length=50,blank=True)

	def __str__(self):
		return self.customer_name
