from django.shortcuts import render, redirect
from inventory.models import hematology_inventory, chemistry_inventory, historical_hematology_inventory, historical_chemistry_inventory, specialist_preferences, specialist_setup
from django.core import serializers
import random
from django.db.models import Q
from django.db.models import Sum
from .forms import hematology_modify_form, hematology_add_form, chemistry_modify_form, chemistry_add_form, specialist_preferences_form
from django.utils.timezone import make_aware
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.apps import apps
from django.contrib.auth.models import User


@staff_member_required
def home_page_specialist(request):


	user_department_selection_specialist= request.session['user_department_selection_specialist']


	#Using get_model to save the model name to the variable department and historical.  Based on user department choice we will then use that model
	#for queries 
	if user_department_selection_specialist == "hematology_inventory":
		department= apps.get_model(app_label="inventory", model_name='hematology_inventory')

	elif user_department_selection_specialist == "chemistry_inventory":
		department= apps.get_model(app_label="inventory", model_name='chemistry_inventory')


	if request.method == 'GET':

		#Handling error that was thrown when page was loaded.  When page was loaded with a get request the reagent_name_table variable was empty.
		#This was throwing an error when it tried to query the database with an empty variable
		#Using is None logic checks if the variable is empty, if it is pass, if not (meaning the user selected a value), perform logic
		
		reagent_lot_from_delete_button= request.GET.get('reagent_lot_from_delete_button')

		#Logic to delete a row if the user wants to delete
		
		#Using the conditional below will perform logic if the user selects delete, if they do not select Delete, reagent_name_from_delete_button
		#Will be None and the logic will not run
		#Checking to see if request is an ajax call

		if reagent_lot_from_delete_button != None:
			if request.is_ajax():



				equation_x= random.randint(0,10)
				equation_y= random.randint(0,10)
				delete_answer= equation_x + equation_y


				return JsonResponse({'reagent_lot_from_delete_button' : reagent_lot_from_delete_button, 'equation_x': equation_x, 
					'equation_y': equation_y, 'delete_answer' : delete_answer})




	#Getting specialist information from form in modal and getting delete object request from user		

	if request.method == "POST":
		
		print(list(request.POST.items()))

		#Since we have two forms, check to see if 'delete-yes-no' is in request.POST, if so run that logic
		if 'user_answer' in request.POST:

			# #Getting value from form

			#Getting equation answer from hidden value and user answer
			equation_answer= request.POST.get('delete_equation_answer')
			user_equation_answer= request.POST.get('user_answer')



			#Querying database with delete_yes_or_no and then deleting if user selects yes
			if equation_answer == user_equation_answer:

				reagent_to_delete= request.POST.get('reagent-lot-to-delete')

				to_delete= department.objects.get(reagent_lot=reagent_to_delete)

				to_delete.delete()

		#Logic for displaying information in top columns:

		if 'specialist_reagent_choice' in request.POST:

			

			specialist_reagent_choice= request.POST['specialist_reagent_choice']
			
			specialist_current_lot_choice= request.POST['specialist_current_lot_choice']




			if request.is_ajax():
				
		
					
				#Checking to see if the specialist chose current lot.
				if specialist_current_lot_choice == "Current lot":


					#Checking to see if the reagent choice and the current lot exist
					if department.objects.filter(Q(reagent_name__iexact=specialist_reagent_choice) & Q(current_lot= True)).exists() == True:
						
						#Getting information about reagent chosen.  Hardcoded current_lot= True since the specialit chose current lot = True.
						table_reagent_name= department.objects.values_list('reagent_name', 'reagent_quantity', 'reagent_lot', 'reagent_lot_expiration',
							'current_lot').get(Q(reagent_name__iexact=specialist_reagent_choice) & Q(current_lot= True))

						#Converting queryset to list
						list_of_reagent_attributes= list(table_reagent_name)

						#Returning the attributes in individual variables
						reagent_name,quantity,lot,expiration,current= list_of_reagent_attributes

						#Setting reagent_exist = True to be passed into AJAX
						reagent_exist= True

						return JsonResponse({'reagent_name' : reagent_name, 'specialist_current_lot_choice' : specialist_current_lot_choice, 'quantity' : quantity,
							'lot' : lot, 'expiration' : expiration, 
							'current' : current, "reagent_exist" : reagent_exist}, status=200)		


					#Checking if the specialist_reagent_choice and current_lot= True exist.
					elif department.objects.filter(Q(reagent_name__iexact=specialist_reagent_choice) & Q(current_lot= True)).exists() == False:

						#Setting reagent_exist = False to be passed into Ajax
						reagent_exist= False

						return JsonResponse({'specialist_reagent_choice' : specialist_reagent_choice, "reagent_exist" : reagent_exist, 
							"specialist_current_lot_choice" : specialist_current_lot_choice}, status=200)								

				
				#Checking to see if specialist did not check current lot
				elif specialist_current_lot_choice == "Not current lot":

					#Checking to see if the reagent name exist
					if department.objects.filter(reagent_name__iexact=specialist_reagent_choice).exists() == True:

						#Filtering the hematology_inventory model ONLY on reagent_name and returing all the lot numbers that have that reagent name
						all_lot_numbers= department.objects.values_list('reagent_lot').filter(reagent_name__iexact=specialist_reagent_choice)

						#Turning the queryset into a list
						tuplelist_of_all_lot_numbers= list(all_lot_numbers)

						#Turing the list of tuples into a list
						list_of_all_lot_numbers= [lot for lot_number in tuplelist_of_all_lot_numbers for lot in lot_number]
						
						#Setting reagent_exist = True
						reagent_exist= True

						return JsonResponse({"reagent_exist" : reagent_exist, 'reagent_name' : specialist_reagent_choice,
						"specialist_current_lot_choice" : specialist_current_lot_choice, "list_of_all_lot_numbers" : list_of_all_lot_numbers})

					#Checking to see if ONLY the reagent name exist
					elif department.objects.filter(reagent_name__iexact=specialist_reagent_choice).exists() == False:

						#Setting reagent_exist = False
						reagent_exist= False

						return JsonResponse({"reagent_exist" : reagent_exist, 'specialist_reagent_choice' : specialist_reagent_choice,
							'specialist_current_lot_choice' : specialist_current_lot_choice})


			
		if 'specialist_lot_choice_from_modal' in request.POST:

			specialist_lot_choice= request.POST['specialist_lot_choice_from_modal']


			if request.is_ajax():

				modal_lot_form_choice= department.objects.values_list('reagent_name', 'reagent_quantity', 'reagent_lot', 'reagent_lot_expiration',
					'current_lot').get(reagent_lot=specialist_lot_choice)
				list_of_attributes_from_modal= list(modal_lot_form_choice)
				reagent_name,quantity,lot,expiration,current= list_of_attributes_from_modal

				#******* THIS WILL ONLY RETURN ONE LOT NUMBER ************
				all_lot_numbers= department.objects.values_list('reagent_lot').get(reagent_lot=specialist_lot_choice)
				tuplelist_of_all_lot_numbers= list(all_lot_numbers)
				list_of_all_lot_numbers= [lot for lot_number in tuplelist_of_all_lot_numbers for lot in lot_number]
				

				return JsonResponse({'reagent_name' : reagent_name, 'quantity' : quantity,
						'lot' : lot, 'expiration' : expiration, 'current' : current, 'list_of_all_lot_numbers' : list_of_all_lot_numbers})



		#This is the request from the modify form.  Takes lot number from table and stores value in hidden field.
		#We will then pass this value into sessions and pass to the view modify

		if 'modify_value' in request.POST:

			modify_lot_value= request.POST['modify_value']

			request.session['modify_lot_value']= modify_lot_value

			return redirect("modify")


		#Checking to see if request.POST contains add_value.  Then redirecting to model form
		#if 'add_value' in request.POST:
			
			#return redirect("add_to_inventory")

		#Checking to see if request.POST contains tech_usage
		#if 'tech_usage' in request.POST:
			
			#return redirect("tech_usage")

		#Checking to see if request.POST contains historical_data.  Then redirecting to historical data html

		if 'historical_value' in request.POST:

			#Getting the lot number of reagent from table
			#Passing lot number to historical_usage view with sessions
			historical_value_table= request.POST['historical_value']

			request.session['historical_value_table']= historical_value_table


			return redirect("historical_usage")

		#if 'specialist-preferences' in request.POST


	#Logic to pass department name into the template based on user selection
	#Checking to see if the logged in user is the specialist for that department
	heme_specialist= request.user.specialist_setup.hematology_specialist
	chemistry_specialist= request.user.specialist_setup.chemistry_specialist


	if user_department_selection_specialist == 'hematology_inventory' and heme_specialist == True:
		department_name= 'Hematology'
		department= hematology_inventory.objects.all()
		labels = []
		data = []
		queryset = hematology_inventory.objects.order_by('reagent_name')
		for reagent in queryset:
			labels.append(reagent.reagent_name)
			data.append(reagent.reagent_quantity)

	elif user_department_selection_specialist == 'chemistry_inventory' and chemistry_specialist == True:
		department_name= 'Chemistry'
		department= chemistry_inventory.objects.all()
		labels = []
		data = []
		queryset = chemistry_inventory.objects.order_by('reagent_name')
		for reagent in queryset:
			labels.append(reagent.reagent_name)
			data.append(reagent.reagent_quantity)

	#Redirecting to home page if the wrong specialist tries to view area they are not a specialist of
	else:
		return redirect("home_page")

	return render(request,'specialist/specialist_information.html',{'department_name' : department_name, 'department' : department,'labels' : labels, 'data' : data})






def modify(request):

	#Department selection passed from sessions
	user_department_selection_specialist= request.session['user_department_selection_specialist']
	
	#Modify value passed from sessions.  Will be used for model instance.
	modify_value_from_table= request.session['modify_lot_value']

	if user_department_selection_specialist == "hematology_inventory":


		#Getting instance of model from sessions value
		reagent_to_modify= hematology_inventory.objects.get(reagent_lot=modify_value_from_table)

		#Making form from this instance and passing to template
		#modify_form= hematology_modify_form(instance=reagent_to_modify)

		if request.method == 'POST':

			#request.POST is the data from our form.  We are checking to see if its valid then saving the data. 
			modify_form= hematology_modify_form(request.POST, instance=reagent_to_modify)

			if modify_form.is_valid():

				modify_form.save()

				return redirect("specialist_information")

		else:
			modify_form= hematology_modify_form(instance=reagent_to_modify)

		#  ****ON FORM SUBMIT REDIRECT BACK TO HUB ****
		return render(request,"specialist/modify.html",{"modify_form" : modify_form})


	elif user_department_selection_specialist == "chemistry_inventory":


		#Getting instance of model from sessions value
		reagent_to_modify=chemistry_inventory.objects.get(reagent_lot=modify_value_from_table)

		#Making form from this instance and passing to template
		#modify_form= hematology_modify_form(instance=reagent_to_modify)

		if request.method == 'POST':

			#request.POST is the data from our form.  We are checking to see if its valid then saving the data. 
			modify_form= chemistry_modify_form(request.POST, instance=reagent_to_modify)

			if modify_form.is_valid():

				modify_form.save()

				return redirect("specialist_information")

		else:
			modify_form= chemistry_modify_form(instance=reagent_to_modify)

		#  ****ON FORM SUBMIT REDIRECT BACK TO HUB ****
		return render(request,"specialist/modify.html",{"modify_form" : modify_form})

def add_to_inventory(request):


	#Department selection passed from sessions
	user_department_selection_specialist= request.session['user_department_selection_specialist']


	if user_department_selection_specialist == "hematology_inventory":

		if request.method == 'POST':

			#request.POST is the data from our form.  We are checking to see if its valid then saving the data. 
			add_form= hematology_add_form(request.POST)

			if add_form.is_valid():

				add_form.save()

				return redirect("specialist_information")

		else:
			add_form= hematology_add_form()


		return render(request,"specialist/add_to_inventory.html",{'add_form' : add_form})

	elif user_department_selection_specialist == "chemistry_inventory":

		if request.method == 'POST':

			#request.POST is the data from our form.  We are checking to see if its valid then saving the data. 
			add_form= chemistry_add_form(request.POST)

			if add_form.is_valid():

				add_form.save()

				return redirect("specialist_information")

		else:
			add_form= chemistry_add_form()


		return render(request,"specialist/add_to_inventory.html",{'add_form' : add_form})


def historical_usage(request):



	user_department_selection_specialist= request.session['user_department_selection_specialist']

	if user_department_selection_specialist == "hematology_inventory":
		department= apps.get_model(app_label="inventory", model_name='hematology_inventory')
		historical_model= apps.get_model(app_label="inventory", model_name='historical_hematology_inventory')

	elif user_department_selection_specialist == "chemistry_inventory":
		department= apps.get_model(app_label="inventory", model_name='chemistry_inventory')
		historical_model= apps.get_model(app_label="inventory", model_name='historical_chemistry_inventory')


	#Getting reagent lot number from sessions
	reagent_lot_from_table= request.session["historical_value_table"]

	#Declaring the two variables below to prevent error.
	historical_reagent=""
	total_usage= ""


	#Checking to see if reagent has even been used to prevent error
	if historical_model.objects.filter(reagent_lot_history= reagent_lot_from_table).exists() == True:


		#Making query to get the name of the reagent from the chosen lot number.  This will return multiple instances if more than one reagent has been used.
		#This will not matter since the reagent name is going to be the same.  We can use first.() to get the first instance.
		historical_reagent= historical_model.objects.filter(reagent_lot_history= reagent_lot_from_table).first()

		#Getting name of reagent to be used in displaying name to user.
		table_reagent_name= historical_model.objects.values_list('reagent_name_history').filter(reagent_lot_history=reagent_lot_from_table).first()
		
		#Converting table_reagent_name into list.  This allows the name to be passed to AJAX
		table_reagent_name_list= list(table_reagent_name)

		#Getting total use of reagent
		total_usage= historical_model.objects.filter(reagent_lot_history=reagent_lot_from_table).aggregate(Sum('reagent_used'))

	else:
		#Making empty list for table_reagent_name_list so an error does not occur.  Error was occuring when table_reagent_name_list was blank 
		#Then passed into AJAX
		table_reagent_name_list=['Does not exist']


	if request.method == "POST":

		
		#if reagent_lot_from_table != None:

		#Getting start_date and end_date from form
		start_date= request.POST['start_date']
		end_date= request.POST['end_date']

	
		#Making query to get queryset containing reagents used on or after start date and on or before end_date.  Taking that queryset and getting the sum.
		time_usage_range= historical_model.objects.filter(Q(reagent_lot_history=reagent_lot_from_table) & Q(reagent_use_date__gte=start_date) 
			& Q(reagent_use_date__lte=end_date)).aggregate(Sum('reagent_used'))



		#Time usage returns a dictionary.  Getting the dictionary value.
		time_usage_range_total= time_usage_range['reagent_used__sum']
		
		#Passing time_usage_total into AJAX.
		if request.is_ajax():

			#Replacing T in string of date with at.  Used in displaying date to user.
			start_date_updated= start_date.replace("T", " at ")
			end_date_updated= end_date.replace("T", " at ")


			return JsonResponse({'time_usage_range_total' : time_usage_range_total, "start_date_updated" : start_date_updated, 
				'end_date_updated' : end_date_updated, 'reagent_name_date_range' : table_reagent_name_list[0], 
				'reagent_lot_from_table' : reagent_lot_from_table}, status=200)

	return render(request, "specialist/historical.html", {'historical_reagent' : historical_reagent, 'total_usage' : total_usage})




def tech_usage(request):


	user_department_selection_specialist= request.session['user_department_selection_specialist']

	if user_department_selection_specialist == "hematology_inventory":
		historical_model= apps.get_model(app_label="inventory", model_name='historical_hematology_inventory')

	elif user_department_selection_specialist == "chemistry_inventory":
		historical_model= apps.get_model(app_label="inventory", model_name='historical_chemistry_inventory')

	#Filtering the historical hematology model to get all uernames 
	all_users= historical_model.objects.values_list('username')
					
	# #Turning the queryset into a set of tuple
	tuplelist_of_all_users= list(set(all_users))

	# #Turing the list of tuples into a list
	list_of_all_users= [users for all_user in tuplelist_of_all_users for users in all_user]
				


	return render(request,"specialist/tech_usage.html", {"list_of_all_users" : list_of_all_users})


def display_tech_usage(request):


	user_department_selection_specialist= request.session['user_department_selection_specialist']

	if user_department_selection_specialist == "hematology_inventory":
		historical_model= apps.get_model(app_label="inventory", model_name='historical_hematology_inventory')

	elif user_department_selection_specialist == "chemistry_inventory":
		historical_model= apps.get_model(app_label="inventory", model_name='historical_chemistry_inventory')



	if request.method == "POST":


	
		if 'start_date_user_usage' in request.POST:

			username_selection= request.POST.get("technologist-selection")
			start_date_user_usage= request.POST.get("start_date_user_usage")
			end_date_user_usage= request.POST.get("end_date_user_usage")


			username= historical_model.objects.filter(Q(username=username_selection) & Q(reagent_use_date__gte=start_date_user_usage) 
				& Q(reagent_use_date__lte=end_date_user_usage))

			#Replacing T in string of date with at.  Used in displaying date to user.
			start_date_user_usage_updated= start_date_user_usage.replace("T", " at ")
			end_date_user_usage_updated= end_date_user_usage.replace("T", " at ")







	
	return render(request,"specialist/display_tech_usage.html",{'username_selection' : username_selection, 'username': username,
		'start_date_user_usage_updated' : start_date_user_usage_updated, 'end_date_user_usage_updated' : end_date_user_usage_updated})




def get_specialist_preferences(request):




	if specialist_preferences.objects.filter(specialist= request.user).exists() == True:

		current_specialist= specialist_preferences.objects.get(specialist= request.user)

		if request.method == 'POST':


			#request.POST is the data from our form.  We are checking to see if its valid then saving the data. 
			set_specialist_preferences= specialist_preferences_form(request.POST, instance= current_specialist)

			if set_specialist_preferences.is_valid():


				instance= set_specialist_preferences.save(commit=False)
				instance.specialist= request.user
				instance.save()

				return redirect("specialist_information")

		else:
			set_specialist_preferences= specialist_preferences_form(instance= current_specialist)


		return render(request,"specialist/specialist_preferences.html",{'set_specialist_preferences' : set_specialist_preferences})

	elif specialist_preferences.objects.filter(specialist= request.user).exists() == False:

		
		if request.method == 'POST':


			#request.POST is the data from our form.  We are checking to see if its valid then saving the data. 
			set_specialist_preferences= specialist_preferences_form(request.POST)

			if set_specialist_preferences.is_valid():


				instance= set_specialist_preferences.save(commit=False)
				instance.specialist= request.user
				instance.save()

				return redirect("specialist_information")

		else:
			set_specialist_preferences= specialist_preferences_form()


		return render(request,"specialist/specialist_preferences.html",{'set_specialist_preferences' : set_specialist_preferences})	