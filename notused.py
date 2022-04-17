#This is code that I tried but ended up not needing

	# #Checking to see if form is a POST request
	# if request.method == "POST":

	# 	#Taking data from form and passing it into our form
	# 	reagent_choice= reagent_choice_form(request.POST)
		
	# 	#Checking to see if form is valid
	# 	if reagent_choice.is_valid():

	# 		#Getting user reagent choice
	# 		user_reagent_selection= reagent_choice.cleaned_data["reagent_choice"]
			
	# 		#Getting amount taken
	# 		user_reagent_amount_taken= reagent_choice.cleaned_data["amount_taken"]

	# 		#Using user_department_choice passed from sessions to query correct model by using if logic
	# 		#Querying database to get the queryset of the reagent the user selected.
	# 		#Using icontains to make the query non case sensitive
	# 		if user_department_choice == 'hematology_inventory':
	# 			user_reagent_choice= hematology_inventory.objects.get(reagent_name__icontains=user_reagent_selection)

	# 			user_reagent_choice.reagent_quantity= F('reagent_quantity') - user_reagent_amount_taken
	# 			user_reagent_choice.save()
					
	# 		#If form is not valid, making a blank form
	# 		return redirect('tech_information_hub')

	# else:
	# 	reagent_choice= reagent_choice_form()



#This code updated the reagent with a modal and form


			#Since we have two forms, check to see if 'form-reagent-name' is in request.POST, if so run that logic
			if 'form-reagent-quantity' in request.POST:		
			
				#Put name from get request in hidden field in HTML.  This is the value of orginal_reagent_name

				reagent_lot= request.POST.get('reagent_lot')
				reagent_name_from_form= request.POST.get("form-reagent-name")
				reagent_quantity_from_form= request.POST.get("form-reagent-quantity")
				lot_number_from_form= request.POST.get("form-lot-number")
				lot_expiration_from_form= request.POST.get("form-lot-expiration")
				current_lot_from_form= request.POST.get("form-current-lot")
				

				#Using reagent name from hidden HTML field to get model entry
				updated_reagent=hematology_inventory.objects.get(reagent_lot=reagent_lot)

				#The block of code below checks to see if the user left a field blank in the modify form
				#This allows the user to leave fields blank if they want without throwing any errors

				

				if reagent_quantity_from_form != '':
					updated_reagent.reagent_quantity= reagent_quantity_from_form

				if lot_number_from_form != '':
					updated_reagent.reagent_lot= lot_number_from_form
				
				if lot_expiration_from_form != '':
					updated_reagent.reagent_lot_expiration= lot_expiration_from_form

				#Current lot from form returns a boolean for true and None for false, using if logic to change current lot to true or false based off form data
				if current_lot_from_form != '':
					if current_lot_from_form == 'True':
						updated_reagent.current_lot= True

					elif current_lot_from_form == None:
						updated_reagent.current_lot = False




				updated_reagent.save()
			



#This code displayed placeholders for the modal form

			#If you chose delete reagent_name_table_specalist will be None, this if conditional prevents an empty queryset error
			if reagent_lot_table_specalist != None:
				#Checking to see if request is an ajax call
				if request.is_ajax():
					
			
						
				 	#Using reagent name from AJAX get call, then getting all the information for that reagent to be passed into form for placeholder
				 	#Getting a tuple of all reagent attributes, turning that into a list, returning attributes into individual variables, passing to JsonResponse 
					table_reagent_name= hematology_inventory.objects.values_list('reagent_name', 'reagent_quantity', 'reagent_lot', 'reagent_lot_expiration',
						'current_lot').get(reagent_lot=reagent_lot_table_specalist)
					list_of_reagent_attributes= list(table_reagent_name)
					reagent_name,quantity,lot,expiration,current= list_of_reagent_attributes


				 	#Passing reagent information into JsonResponse
					return JsonResponse({'reagent_name' : reagent_name, 'quantity' : quantity,
						'lot' : lot, 'expiration' : expiration, 'current' : current}, status=200)