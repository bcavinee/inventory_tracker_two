from django.forms import ModelForm, widgets
from inventory.models import hematology_inventory, chemistry_inventory, specialist_preferences
from django import forms




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
