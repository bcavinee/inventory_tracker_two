from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from inventory.models import specialist_setup
from django import forms


class specialist_setup_admin(forms.ModelForm):

	class Meta:

		model= specialist_setup

		fields= "__all__"


	def clean(self):

		hematology_specialist_admin= self.cleaned_data.get("hematology_specialist")
		chemistry_specialist_admin= self.cleaned_data.get("chemistry_specialist")
		
		if hematology_specialist_admin == True and chemistry_specialist_admin == True:

			# self.cleaned_data= super().clean()
			# self.cleaned_data['hematology_specialist'] = False
			# return self.cleaned_data
			# self.cleaned_data= super().clean()
			# self.cleaned_data['_specialist'] = False
			# return self.cleaned_data

			#Setting messages = to a validation error
			message= forms.ValidationError("Only one person can be the specialist of a department")
			#Then adding this error to the alert_for_expiration field and displaying the message.  This will make it so the form 
			#cannot be submitted if the user did not select number of days.
			self.add_error("hematology_specialist", message)
			self.add_error("chemistry_specialist", message)			

		# elif specialist_setup.objects.filter(hematology_specialist= True).exists() == True and hematology_specialist_admin == True:
		# 	specialist_setup.objects.filter(hematology_specialist= True).update(hematology_specialist= False)
			
			
		# 	return self.cleaned_data


		# elif specialist_setup.objects.filter(chemistry_specialist= True).exists() == True and chemistry_specialist_admin == True:
		# 	specialist_setup.objects.filter(chemistry_specialist= True).update(chemistry_specialist= False)
			
		# 	return self.cleaned_data

		return self.cleaned_data
	


class specialist_inline(admin.StackedInline):

	model= specialist_setup
	form= specialist_setup_admin
	can_delete= False
	verbose_name = 'Specialist Setup'
	verbose_name_plural= "Specialist Setup"

class UserAdmin(BaseUserAdmin):
	inlines= (specialist_inline,)
	


admin.site.unregister(User)
admin.site.register(User, UserAdmin)



