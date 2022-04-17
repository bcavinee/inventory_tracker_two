from django.shortcuts import render, redirect
from .forms import department_selection_form, department_selection_specialist_form
from .models import hematology_inventory, chemistry_inventory, historical_hematology_inventory, historical_chemistry_inventory, specialist_preferences, specialist_setup
from django.db.models import F
from django.http import JsonResponse
from django.db.models import Q
from django.apps import apps
from django.core.mail import send_mail
import time
from django.contrib.auth.models import User
from datetime import date, timedelta

def base(request):


	return render(request,'inventory/base.html')


def home_page(request):

	
	
	
	user_department_selection_form= department_selection_form()
	specialist_selection_form= department_selection_specialist_form()

	#Checking to see if form is a POST request
	if request.method == "POST":

		
		#Since we have two forms we must use a conditional to see what form is being submitted, if not the form that is not used
		#Will be expecting information and throw an error
		#request.POST contains the name of the submit button, I named the submit button in tech department selection, tech_department_selection
		#When we use the statement if 'tech_department_selection' in request.POST:, we are checking to see if 'tech_department_selection' is in
		#The post request
		if 'tech_department_selection' in request.POST:

			#Taking data from form and passing it into our form
			user_department_selection_form= department_selection_form(request.POST)

			#Checking to see if form is valid
			if user_department_selection_form.is_valid():
				

				#Getting user department selection
				user_department_selection= user_department_selection_form.cleaned_data['department_selection']

				#Using sessions to pass the department selection to tech_information_hub view
				request.session['user_department_selection']= user_department_selection

				return redirect('tech_information_hub')

		if 'specialist_department_selection' in request.POST:

			#Taking data from form and passing it into our form
			specialist_selection_form= department_selection_specialist_form(request.POST)

			#Checking to see if form is valid
			if specialist_selection_form.is_valid():

				#Getting user department selection
				user_department_selection_specialist= specialist_selection_form.cleaned_data['department_selection_specialist']


				#Using sessions to pass the department selection to tech_information_hub view
				request.session['user_department_selection_specialist']= user_department_selection_specialist

				return redirect('specialist_information')


	#If form is not valid, making a blank form
	else:

		user_department_selection_form= department_selection_form()
		specialist_selection_form= department_selection_specialist_form()


	
	class check_expiration:

		#*********************  YOU CAN PROBABLY USE CLASS VARIABLES FOR SOME OF THIS.  LOOK AT REPEATED CODE WHEN YOU MAKE AN INSTANCE. ***********************

		specialist_setup_model= apps.get_model(app_label="inventory", model_name= "specialist_setup")
		specialist_preferences_model= apps.get_model(app_label="inventory", model_name= "specialist_preferences")


		def __init__(self,department,specialist_reagent_model):

			self.department= department
			self.specialist_reagent_model= apps.get_model(app_label="inventory", model_name= specialist_reagent_model)


		def send_expiration_email(self):

			#Getting all the specialist in model
			all_specialist= check_expiration.specialist_setup_model.objects.all()
			specialist_user= None

			#Looping through specialist in model
			for specialist in all_specialist:
				#Getting a dict of all the attributes of the specialist setup model
				dict_of_attributes= specialist.__dict__
				#If the specialist is == the department from our instance.  Return that model object to specialist_user
				if dict_of_attributes[self.department] == True:
					specialist_user= specialist

			#Getting the specialist email
			specialist_email= specialist_user.user.email
			#Getting the specalist preferences model by using the user from specialist user.
			specialist_data= check_expiration.specialist_preferences_model.objects.get(specialist=specialist_user.user)
			#Getting the number of days that the specialist selected to be notified of expiration 
			specialist_alert= specialist_data.alert_for_expiration
			specialist_alert_boolean= specialist_data.alert_for_expiration_yes_or_no

			#Checking if the user selects to have emails 

			if specialist_alert_boolean == True:
			
				#Getting all of the reagents in the instance from self.specialist_reagent_model
				reagent_lots= self.specialist_reagent_model.objects.values_list('reagent_lot', flat=True)
				#Turning this into a list
				reagent_lot_list= list(reagent_lots)
				
				#Looping through each reagent and checking its expiration date and send_email value.  Then getting a time delta.
				#If the time delta is less than or equal to the alert value the specialist selected.
				#Send email
				for reagent_lot in reagent_lot_list:
					
					reagent_for_email= self.specialist_reagent_model.objects.get(reagent_lot= reagent_lot)

					todays_date= date.today()
					expiration_date= reagent_for_email.reagent_lot_expiration
					delta= (expiration_date - todays_date).days				

					email_sent= reagent_for_email.email_sent

					if delta <= specialist_alert and email_sent == False:

						
						send_mail("Reagent Expiration Warning",f"Warning {reagent_for_email.reagent_name} Lot: {reagent_lot} has expired",
							"bcavinee@gmail.com",[specialist_email], fail_silently=False)	

						set_sent_email_true= self.specialist_reagent_model.objects.get(reagent_lot= reagent_lot)
						set_sent_email_true.email_sent= True
						set_sent_email_true.save()


	hematology= check_expiration("hematology_specialist","hematology_inventory")
	hematology.send_expiration_email()
	chemistry= check_expiration("chemistry_specialist","chemistry_inventory")
	chemistry.send_expiration_email()

	return render(request,'inventory/home_page.html',{'user_department_selection_form' : user_department_selection_form,
		'specialist_selection_form' : specialist_selection_form})



def tech_information_hub(request):

	
	

	user_department_choice= request.session['user_department_selection']

	#Using get_model to save the model name to the variable department and historical.  Based on user department choice we will then use that model
	#for queries.  Setting specialist to true based on department choice.  Getting speca
	if user_department_choice == "hematology_inventory":

		department= apps.get_model(app_label="inventory", model_name='hematology_inventory')
		historical= apps.get_model(app_label="inventory", model_name='historical_hematology_inventory')
		specialist= specialist_setup.objects.get(hematology_specialist= True)
		specialist_name= specialist.user
		specialist_email= specialist.user.email

	elif user_department_choice == "chemistry_inventory":
			
		department= apps.get_model(app_label="inventory", model_name='chemistry_inventory')
		historical= apps.get_model(app_label="inventory", model_name='historical_chemistry_inventory')
		specialist= specialist_setup.objects.get(chemistry_specialist= True)
		specialist_name= specialist.user
		specialist_email= specialist.user.email

	#Getting the user that is logged in for tracking
	current_user= request.user

	#Then saving a string of the users first and last name
	user_first_last= current_user.first_name +  " " + current_user.last_name
	
	if request.method == 'POST':
		
		#Getting reagent choice and amount taken from form with AJAX
		reagent_user_choice= request.POST['reagent_choice']
		amount_taken= request.POST['amount_taken']

		


		#Getting user reagent choice by querying hematology_inventory model
		#Using Q object to check if reagent is the current lot
		#Checking to see if reagent_user_choice exist.  If so then update the reagent, if not pass false into AJAX and display message
		#Stating reagent does not exist
		if department.objects.filter(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True)).exists() == True:

			user_reagent_choice= department.objects.get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True))
			

			#Taking amount taken by user and decrementing the reagent quantity in database 
			user_reagent_choice.reagent_quantity= F('reagent_quantity') - amount_taken

			
			#Saving the updated reagent quantity
			user_reagent_choice.save()

		
			#Getting value of reagent lot number to be used in historical model instance (**ALSO USING THIS FOR EMAIL**)
			reagent_lot_for_historical= department.objects.values_list('reagent_lot', flat=True).get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot= True))

			#Getting value of reagent_name for historical model instance 
			reagent_name_for_historical= department.objects.values_list('reagent_name', flat=True).get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot= True))

			#Creating a historical model instance

			historical.objects.create(reagent_used= amount_taken, reagent_name_history= reagent_name_for_historical, 
				reagent_lot_history= reagent_lot_for_historical, username=user_first_last)

			#Getting specialist preferences based on what specialist is logged in
			alert_if_low= specialist_preferences.objects.values_list('alert_when_low', flat=True).get(specialist=specialist_name)
			alert_if_empty= specialist_preferences.objects.values_list('alert_when_empty', flat=True).get(specialist=specialist_name)
			specialist_warning_level= department.objects.values_list('warning_amount', flat=True).get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True))
			amount_remaining= department.objects.values_list('reagent_quantity', flat=True).get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True))

			#Checking specialist preferences and then sending email
			if alert_if_low == True and amount_remaining <= specialist_warning_level:

				#*******IMPORTANT******* IN PRODUCTION THIS IS WERE YOU WOULD PUT THE LOGED IN USERS EMAIL
				send_mail("Low Reagent Warning",f"Warning {reagent_user_choice} Lot: {reagent_lot_for_historical} has {amount_remaining} remaining",
					"bcavinee@gmail.com",[specialist_email], fail_silently=False)

			#Checking specialist preferences and then sending email
			if alert_if_empty == True and amount_remaining == 0:

				#*******IMPORTANT******* IN PRODUCTION THIS IS WERE YOU WOULD PUT THE LOGED IN USERS EMAIL
				send_mail("Empty Reagent Warning",f"Warning {reagent_user_choice} Lot: {reagent_lot_for_historical} is depleted",
					"bcavinee@gmail.com",[specialist_email], fail_silently=False)				
			
			#Checking to see if request is an ajax call
			reagent_exist= True
			if request.is_ajax():
				

				#Getting updated reagent amount value by using value_list to get the reagent quantity, then using a get call to target the specific reagent
				#Getting warning level to pass into AJAX.
				warning_level= department.objects.values_list('warning_amount', flat=True).get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True))
				updated_reagent_amount= department.objects.values_list('reagent_quantity', flat=True).get(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True))
				#Passing the reagent name the user selected and the updated reagent amount to the ajax call with a JsonResponse

				return JsonResponse({'reagent_name': reagent_user_choice,'updated_reagent_amount' : updated_reagent_amount, 'reagent_exist' : reagent_exist,
					'warning_level' : warning_level}, status=200)

		elif department.objects.filter(Q(reagent_name__iexact=reagent_user_choice) & Q(current_lot=True)).exists() == False:
			
			reagent_exist= False

			if request.is_ajax():

				return JsonResponse({'reagent_exist': reagent_exist, 'reagent_name' : reagent_user_choice}, status=200)



	
	elif request.method == 'GET':

		#Below is all for hematology

		#Handling error that was thrown when page was loaded.  When page was loaded with a get request the reagent_name_table variable was empty.
		#This was throwing an error when it tried to query the database with an empty variable
		#Using is None logic checks if the variable is empty, if it is pass, if not (meaning the user selected a value), perform logic
		reagent_lot_table= request.GET.get('reagent_lot_from_table')
		

		

		if reagent_lot_table is None:
			pass

		elif reagent_lot_table is not None:
			
			#Getting user reagent choice by querying hematology_inventory model
			user_reagent_choice_table= department.objects.get(reagent_lot=reagent_lot_table)

			#Taking amount taken by user and decrementing the reagent quantity in database 
			user_reagent_choice_table.reagent_quantity= F('reagent_quantity') - 1

			#Saving the updated reagent quantity
			user_reagent_choice_table.save()

			#Getting value of reagent lot number to be used in historical model instance (**ALSO USING THIS FOR EMAIL**)
			reagent_lot_for_historical_table= department.objects.values_list('reagent_lot', flat=True).get(reagent_lot=reagent_lot_table)

			#Getting the reagent name from table to be used in historical model instance (**ALSO USING THIS FOR EMAIL**)
			reagent_name_for_historical_table= department.objects.values_list('reagent_name', flat=True).get(reagent_lot=reagent_lot_table)

			#Creating a historical model instance
			historical.objects.create(reagent_used= 1, reagent_name_history= reagent_name_for_historical_table, 
				reagent_lot_history= reagent_lot_for_historical_table, username=user_first_last)

			#Getting specialist preferences based on what specialist is logged in
			alert_if_low= specialist_preferences.objects.values_list('alert_when_low', flat=True).get(specialist=specialist_name)
			alert_if_empty= specialist_preferences.objects.values_list('alert_when_empty', flat=True).get(specialist=specialist_name)
			specialist_warning_level= department.objects.values_list('warning_amount', flat=True).get(Q(reagent_name__iexact=user_reagent_choice_table) & Q(current_lot=True))
			amount_remaining= department.objects.values_list('reagent_quantity', flat=True).get(Q(reagent_name__iexact=user_reagent_choice_table) & Q(current_lot=True))

			#Checking specialist preferences and then sending email
			if alert_if_low == True and amount_remaining <= specialist_warning_level:

				#*******IMPORTANT******* IN PRODUCTION THIS IS WERE YOU WOULD PUT THE LOGED IN USERS EMAIL
				send_mail("Low Reagent Warning",f"Warning {user_reagent_choice_table} Lot: {reagent_lot_for_historical_table} has {amount_remaining} remaining",
					"bcavinee@gmail.com",[specialist_email], fail_silently=False)

			#Checking specialist preferences and then sending email
			if alert_if_empty == True and amount_remaining == 0:

				#*******IMPORTANT******* IN PRODUCTION THIS IS WERE YOU WOULD PUT THE LOGED IN USERS EMAIL
				send_mail("Empty Reagent Warning",f"Warning {reagent_name_for_historical_table} Lot: {reagent_lot_for_historical_table} is depleted",
					"bcavinee@gmail.com",[specialist_email], fail_silently=False)					

			#Checking to see if request is an ajax call
			if request.is_ajax():
				
				#Getting updated reagent amount value by using value_list to get the reagent quantity, then using a get call to target the specific reagent
				table_updated_reagent_amount= department.objects.values_list('reagent_quantity', flat=True).get(reagent_lot=reagent_lot_table)
				reagent_warning_level= department.objects.values_list('warning_amount', flat=True).get(reagent_lot=reagent_lot_table)

				#Passing the reagent name the user selected and the updated reagent amount to the ajax call with a JsonResponse
				return JsonResponse({'table_updated_reagent_amount' : table_updated_reagent_amount, 'reagent_warning_level' : reagent_warning_level}, status=200)




	#Logic to pass department name into the template based on user selection
	if user_department_choice == 'hematology_inventory':
		department_name= 'Hematology'
		department= hematology_inventory.objects.all()

	elif user_department_choice == 'chemistry_inventory':
		department_name= 'Chemistry'
		department= chemistry_inventory.objects.all()







	return render(request,'inventory/tech_information_hub.html', {'department_name' : department_name, 'department' : department})

	#return render(request,'inventory/tech_information_hub.html',{'reagent_choice' : reagent_choice, 'user_reagent_choice' : user_reagent_choice})

