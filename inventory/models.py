from django.db import models
from datetime import datetime  
from django.utils import timezone
from django.contrib.auth.models import User

#Modals to store chemistry and hematology data

class hematology_inventory(models.Model):

	reagent_name= models.CharField(max_length=200)
	reagent_lot= models.CharField(max_length=100, unique=True)
	reagent_lot_expiration= models.DateField()
	current_lot= models.BooleanField()
	reagent_quantity= models.IntegerField()
	warning_amount= models.IntegerField()
	email_sent= models.BooleanField(default=False)

	#Overriding the save method.  Checking to see if the new model instance reagent_name already exist and if its current lot is True.
	#If True getting all of the reagents with that name and updating the current_lot to False.
	#Then setting the new model instance to True.
	def save(self, *args, **kwargs):
		if hematology_inventory.objects.filter(reagent_name=self.reagent_name).exists() == True and self.current_lot == True:
			hematology_inventory.objects.filter(reagent_name=self.reagent_name).update(current_lot= False)
			self.current_lot= True
		super(hematology_inventory,self).save(*args,**kwargs)
			
	class Meta:
	   	verbose_name = 'Hematology Inventory'
	   	verbose_name_plural = 'Hematology Inventory'

	def __str__(self):
		return self.reagent_name 



class historical_hematology_inventory(models.Model):

	reagent_used= models.IntegerField()
	reagent_use_date= models.DateTimeField(default=timezone.now, blank=True)
	reagent_name_history= models.CharField(max_length=100)
	reagent_lot_history= models.IntegerField()
	username= models.CharField(max_length=100)


	class Meta:
	   	verbose_name = 'Historical Hematology Inventory'
	   	verbose_name_plural = 'Historical Hematology Inventory'


	def __str__(self):
		return self.reagent_name_history


# class hematology_user_data(models.Model):

# 	username= models.CharField(max_length=100)
# 	reagent_taken= models.CharField(max_length=100)
# 	amount_taken= models.IntegerField()
# 	reagent_lot= models.IntegerField()
# 	reagent_use_date= models.DateTimeField(default=timezone.now, blank=True)	


# 	class Meta:
# 	   	verbose_name = 'Technologist Usage Data'
# 	   	verbose_name_plural = 'Technologist Usage Data'


# 	def __str__(self):
# 		return self.username		

class chemistry_inventory(models.Model):

	reagent_name= models.CharField(max_length=200)
	reagent_lot= models.CharField(max_length=100, unique=True)
	reagent_lot_expiration= models.DateField()
	current_lot= models.BooleanField()
	reagent_quantity= models.IntegerField()
	warning_amount= models.IntegerField()
	email_sent= models.BooleanField(default=False)
	
	#Overriding the save method.  Checking to see if the new model instance reagent_name already exist and if its current lot is True.
	#If True getting all of the reagents with that name and updating the current_lot to False.
	#Then setting the new model instance to True.
	def save(self, *args, **kwargs):
		if chemistry_inventory.objects.filter(reagent_name=self.reagent_name).exists() == True and self.current_lot == True:
			chemistry_inventory.objects.filter(reagent_name=self.reagent_name).update(current_lot= False)
			self.current_lot= True
		super(chemistry_inventory,self).save(*args,**kwargs)
			
	class Meta:
	   	verbose_name = 'Chemistry Inventory'
	   	verbose_name_plural = 'Chemistry Inventory'

	def __str__(self):
		return self.reagent_name 



class historical_chemistry_inventory(models.Model):

	reagent_used= models.IntegerField()
	reagent_use_date= models.DateTimeField(default=timezone.now, blank=True)
	reagent_name_history= models.CharField(max_length=100)
	reagent_lot_history= models.IntegerField()
	username= models.CharField(max_length=100)


	class Meta:
	   	verbose_name = 'Historical Chemistry Inventory'
	   	verbose_name_plural = 'Historical Chemistry Inventory'


	def __str__(self):
		return self.reagent_name_history


class specialist_preferences(models.Model):

	specialist= models.ForeignKey(User, on_delete=models.CASCADE)
	alert_when_low= models.BooleanField(help_text="Email will be sent when reagent gets to warning level")
	alert_for_expiration_yes_or_no= models.BooleanField()
	alert_for_expiration= models.IntegerField(help_text="Chose days before expiration to receive a warning email ")
	alert_when_empty= models.BooleanField(help_text= "Send email when reagent is empty")

	class Meta:
	   	verbose_name = 'Specialist Preferences'
	   	verbose_name_plural = 'Specialist Preferences'

	def __str__(self):
		message= str(self.specialist)
		return message + " Preferences"


class specialist_setup(models.Model):

	user= models.OneToOneField(User, on_delete= models.CASCADE)
	hematology_specialist= models.BooleanField(unique= True)
	chemistry_specialist= models.BooleanField(unique= True)