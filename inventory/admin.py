from django.contrib import admin
from .models import hematology_inventory, chemistry_inventory, historical_hematology_inventory, historical_chemistry_inventory, specialist_preferences
from django import forms

admin.site.register(hematology_inventory)
admin.site.register(chemistry_inventory)
admin.site.register(historical_hematology_inventory)
admin.site.register(historical_chemistry_inventory)


class preferences_admin(forms.ModelForm):

	class Meta:

		model= specialist_preferences

		exclude= ["specialist"]


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

class specialist_preferences_admin(admin.ModelAdmin):
	
	form= preferences_admin


admin.site.register(specialist_preferences,specialist_preferences_admin)
# admin.site.register(hematology_user_data)