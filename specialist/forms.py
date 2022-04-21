from django.forms import ModelForm, widgets
from inventory.models import hematology_inventory, chemistry_inventory, specialist_preferences
from django import forms
from django.contrib import admin



class hematology_modify_form(ModelForm):

	class Meta:
		model= hematology_inventory
		exclude= ('email_sent',)

		widgets= {

		'reagent_lot_expiration': widgets.DateInput(attrs={'type': 'date'})
		}


class hematology_add_form(ModelForm):

	class Meta:
		model= hematology_inventory
		exclude= ('email_sent',)

		widgets= {

		'reagent_lot_expiration': widgets.DateInput(attrs={'type': 'date'})
		}


class chemistry_modify_form(ModelForm):

	class Meta:
		model= chemistry_inventory
		exclude= ('email_sent',)

		widgets= {

		'reagent_lot_expiration': widgets.DateInput(attrs={'type': 'date'})
		}


class chemistry_add_form(ModelForm):

	class Meta:
		model= chemistry_inventory
		exclude= ('email_sent',)

		widgets= {

		'reagent_lot_expiration': widgets.DateInput(attrs={'type': 'date'})
		}


class specialist_preferences_form(ModelForm):

	class Meta:
		model= specialist_preferences
		
		exclude = ['specialist']

		labels= {
		"alert_for_expiration_yes_or_no" : "Check box if you would like to receive expiration emails"
		}


	def clean(self):

		#Getting the values of alert_for_expiration_yes_or_no and alert_for_expiration from form
		alert_boolean= self.cleaned_data.get("alert_for_expiration_yes_or_no")
		days_for_alert= self.cleaned_data.get("alert_for_expiration")

		#Checking to see if the user chose to have emails sent but did not select how many days for expiration
		if alert_boolean == True and days_for_alert == None:

			#Setting messages = to a validation error
			message= forms.ValidationError("This field is required")
			#Then adding this error to the alert_for_expiration field and displaying the message.  This will make it so the form 
			#cannot be submitted if the user did not select number of days.
			self.add_error("alert_for_expiration", message)

		#Same logic as above but checking to see if the user chose and amount of days but did not select send email.
		elif alert_boolean == False and days_for_alert != None:

			message= forms.ValidationError("Must check box to receive emails")
			self.add_error("alert_for_expiration_yes_or_no", message)



		return self.cleaned_data


# class preferences_admin(admin.ModelAdmin):

# 	class Meta:

# 		model= specialist_preferences

# 		exclude= ["specialist"]


# 	def clean(self):

# 		#Getting the values of alert_for_expiration_yes_or_no and alert_for_expiration from form
# 		alert_boolean= self.cleaned_data.get("alert_for_expiration_yes_or_no")
# 		days_for_alert= self.cleaned_data.get("alert_for_expiration")

# 		#Checking to see if the user chose to have emails sent but did not select how many days for expiration
# 		if alert_boolean == True and days_for_alert == None:

# 			#Setting messages = to a validation error
# 			message= forms.ValidationError("This field is required")
# 			#Then adding this error to the alert_for_expiration field and displaying the message.  This will make it so the form 
# 			#cannot be submitted if the user did not select number of days.
# 			self.add_error("alert_for_expiration", message)

# 		#Same logic as above but checking to see if the user chose and amount of days but did not select send email.
# 		elif alert_boolean == False and days_for_alert != None:

# 			message= forms.ValidationError("Must check box to receive emails")
# 			self.add_error("alert_for_expiration_yes_or_no", message)



# 		return self.cleaned_data