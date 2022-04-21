from django import forms
from django.forms import ModelForm
from .models import hematology_inventory

#Form to direct user to different department hub

#Tuple containing choices of department
department_choices= [

	('hematology_inventory','Hematology'),
	('chemistry_inventory', 'Chemistry')

]



#Form with choice of departments
class department_selection_form(forms.Form):

	department_selection= forms.CharField(widget=forms.Select(choices=department_choices),label=False)





class department_selection_specialist_form(forms.Form):

	department_selection_specialist= forms.CharField(widget=forms.Select(choices=department_choices),label=False)


