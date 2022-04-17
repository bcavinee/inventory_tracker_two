#ITERATION ONE


heme_specialist= specialist_setup.objects.get(hematology_specialist= True)
heme_specialist_name= heme_specialist.user
heme_specialist_email= heme_specialist.user.email
# print(heme_specialist.user.email)

#Getting the hematology specialist alert value
specialist_data= specialist_preferences.objects.get(specialist=heme_specialist_name)
specialist_alert= specialist_data.alert_for_expiration

reagent_lots= hematology_inventory.objects.values_list('reagent_lot', flat=True)
reagent_lots_list= list(reagent_lots)


#for (expiration,reagent_name,reagent_lot,email_sent) in zip(reagent_expirations_list,reagent_names_list,reagent_lots_list, email_sent_value_list):
for reagent_lot in reagent_lots_list:

	reagent_info= hematology_inventory.objects.get(reagent_lot=reagent_lot)

	todays_date= date.today()
	expiration_date= reagent_info.reagent_lot_expiration
	delta= (expiration_date - todays_date).days

	email_sent= reagent_info.email_sent

	if delta <= specialist_alert and email_sent == False:

		
		send_mail("Empty Reagent Warning",f"Warning {reagent_info.reagent_name} Lot: {reagent_lot} has expired",
			"bcavinee@gmail.com",[heme_specialist_email], fail_silently=False)	

		set_sent_email_true= hematology_inventory.objects.get(reagent_lot= reagent_lot)
		set_sent_email_true.email_sent= True
		set_sent_email_true.save()

heme_specialist= specialist_setup.objects.get(hematology_specialist= True)
heme_specialist_name= heme_specialist.user
heme_specialist_email= heme_specialist.user.email
# print(heme_specialist.user.email)

#Getting the hematology specialist alert value
specialist_data= specialist_preferences.objects.get(specialist=heme_specialist_name)
specialist_alert= specialist_data.alert_for_expiration

reagent_lots= hematology_inventory.objects.values_list('reagent_lot', flat=True)
reagent_lots_list= list(reagent_lots)


#for (expiration,reagent_name,reagent_lot,email_sent) in zip(reagent_expirations_list,reagent_names_list,reagent_lots_list, email_sent_value_list):
for reagent_lot in reagent_lots_list:

	reagent_info= hematology_inventory.objects.get(reagent_lot=reagent_lot)

	todays_date= date.today()
	expiration_date= reagent_info.reagent_lot_expiration
	delta= (expiration_date - todays_date).days

	email_sent= reagent_info.email_sent

	if delta <= specialist_alert and email_sent == False:

		
		send_mail("Empty Reagent Warning",f"Warning {reagent_info.reagent_name} Lot: {reagent_lot} has expired",
			"bcavinee@gmail.com",[heme_specialist_email], fail_silently=False)	

		set_sent_email_true= hematology_inventory.objects.get(reagent_lot= reagent_lot)
		set_sent_email_true.email_sent= True
		set_sent_email_true.save()
heme_specialist= specialist_setup.objects.get(hematology_specialist= True)
heme_specialist_name= heme_specialist.user
heme_specialist_email= heme_specialist.user.email
# print(heme_specialist.user.email)

#Getting the hematology specialist alert value
specialist_data= specialist_preferences.objects.get(specialist=heme_specialist_name)
specialist_alert= specialist_data.alert_for_expiration

reagent_lots= hematology_inventory.objects.values_list('reagent_lot', flat=True)
reagent_lots_list= list(reagent_lots)


#for (expiration,reagent_name,reagent_lot,email_sent) in zip(reagent_expirations_list,reagent_names_list,reagent_lots_list, email_sent_value_list):
for reagent_lot in reagent_lots_list:

	reagent_info= hematology_inventory.objects.get(reagent_lot=reagent_lot)

	todays_date= date.today()
	expiration_date= reagent_info.reagent_lot_expiration
	delta= (expiration_date - todays_date).days

	email_sent= reagent_info.email_sent

	if delta <= specialist_alert and email_sent == False:

		
		send_mail("Empty Reagent Warning",f"Warning {reagent_info.reagent_name} Lot: {reagent_lot} has expired",
			"bcavinee@gmail.com",[heme_specialist_email], fail_silently=False)	

		set_sent_email_true= hematology_inventory.objects.get(reagent_lot= reagent_lot)
		set_sent_email_true.email_sent= True
		set_sent_email_true.save()
heme_specialist= specialist_setup.objects.get(hematology_specialist= True)
heme_specialist_name= heme_specialist.user
heme_specialist_email= heme_specialist.user.email
# print(heme_specialist.user.email)

#Getting the hematology specialist alert value
specialist_data= specialist_preferences.objects.get(specialist=heme_specialist_name)
specialist_alert= specialist_data.alert_for_expiration

reagent_lots= hematology_inventory.objects.values_list('reagent_lot', flat=True)
reagent_lots_list= list(reagent_lots)


#for (expiration,reagent_name,reagent_lot,email_sent) in zip(reagent_expirations_list,reagent_names_list,reagent_lots_list, email_sent_value_list):
for reagent_lot in reagent_lots_list:

	reagent_info= hematology_inventory.objects.get(reagent_lot=reagent_lot)

	todays_date= date.today()
	expiration_date= reagent_info.reagent_lot_expiration
	delta= (expiration_date - todays_date).days

	email_sent= reagent_info.email_sent

	if delta <= specialist_alert and email_sent == False:

		
		send_mail("Empty Reagent Warning",f"Warning {reagent_info.reagent_name} Lot: {reagent_lot} has expired",
			"bcavinee@gmail.com",[heme_specialist_email], fail_silently=False)	

		set_sent_email_true= hematology_inventory.objects.get(reagent_lot= reagent_lot)
		set_sent_email_true.email_sent= True
		set_sent_email_true.save()
heme_specialist= specialist_setup.objects.get(hematology_specialist= True)
heme_specialist_name= heme_specialist.user
heme_specialist_email= heme_specialist.user.email
# print(heme_specialist.user.email)

#Getting the hematology specialist alert value
specialist_data= specialist_preferences.objects.get(specialist=heme_specialist_name)
specialist_alert= specialist_data.alert_for_expiration

reagent_lots= hematology_inventory.objects.values_list('reagent_lot', flat=True)
reagent_lots_list= list(reagent_lots)


#for (expiration,reagent_name,reagent_lot,email_sent) in zip(reagent_expirations_list,reagent_names_list,reagent_lots_list, email_sent_value_list):
for reagent_lot in reagent_lots_list:

	reagent_info= hematology_inventory.objects.get(reagent_lot=reagent_lot)

	todays_date= date.today()
	expiration_date= reagent_info.reagent_lot_expiration
	delta= (expiration_date - todays_date).days

	email_sent= reagent_info.email_sent

	if delta <= specialist_alert and email_sent == False:

		
		send_mail("Empty Reagent Warning",f"Warning {reagent_info.reagent_name} Lot: {reagent_lot} has expired",
			"bcavinee@gmail.com",[heme_specialist_email], fail_silently=False)	

		set_sent_email_true= hematology_inventory.objects.get(reagent_lot= reagent_lot)
		set_sent_email_true.email_sent= True
		set_sent_email_true.save()



#Iteration Two

class check_expiration:

	
	specialist_preferences= None
	specialist_alert= None
	model_for_reagent_lot= None
	def __init__(self,specialist_name):

		self.specialist_name= specialist_name
		if self.specialist_name == "hematology":
		
			check_expiration.specialist_preferences= specialist_setup.objects.get(hematology_specialist= True)
			check_expiration.specialist_alert=specialist_preferences.objects.get(specialist=check_expiration.specialist_preferences.user)
			check_expiration.model_for_reagent_lot= apps.get_model(app_label="inventory", model_name='hematology_inventory')
			
		elif self.specialist_name == "chemistry":

			check_expiration.specialist_preferences= specialist_setup.objects.get(chemistry_specialist= True)
			check_expiration.specialist_alert= specialist_preferences.objects.get(specialist=check_expiration.specialist_preferences.user)
			check_expiration.model_for_reagent_lot= apps.get_model(app_label="inventory", model_name='chemistry_inventory')

		elif self.specialist_name == "chemistry":

			check_expiration.specialist_preferences= specialist_setup.objects.get(chemistry_specialist= True)
			check_expiration.specialist_alert= specialist_preferences.objects.get(specialist=check_expiration.specialist_preferences.user)
			check_expiration.model_for_reagent_lot= apps.get_model(app_label="inventory", model_name='chemistry_inventory')			

		elif self.specialist_name == "chemistry":

			check_expiration.specialist_preferences= specialist_setup.objects.get(chemistry_specialist= True)
			check_expiration.specialist_alert= specialist_preferences.objects.get(specialist=check_expiration.specialist_preferences.user)
			check_expiration.model_for_reagent_lot= apps.get_model(app_label="inventory", model_name='chemistry_inventory')
		elif self.specialist_name == "chemistry":

			check_expiration.specialist_preferences= specialist_setup.objects.get(chemistry_specialist= True)
			check_expiration.specialist_alert= specialist_preferences.objects.get(specialist=check_expiration.specialist_preferences.user)
			check_expiration.model_for_reagent_lot= apps.get_model(app_label="inventory", model_name='chemistry_inventory')

	@classmethod
	def send_expiration_email(cls):
	
		reagent_info= cls.model_for_reagent_lot.objects.values_list('reagent_lot', flat=True)
		reagent_lot_list= list(reagent_info)

		for reagent_lot in reagent_lot_list:
			
			reagent_for_email= cls.model_for_reagent_lot.objects.get(reagent_lot= reagent_lot)

			todays_date= date.today()
			expiration_date= reagent_for_email.reagent_lot_expiration
			delta= (expiration_date - todays_date).days				

			email_sent= reagent_for_email.email_sent
			print(email_sent)
			

hematology_specialist= check_expiration("hematology")
chemistry_specialist= check_expiration("chemistry")

li= ["hematology", "chemistry"]
for x in li:
	specialist= check_expiration(x)
	specialist.send_expiration_email()		

class check_expiration:


	def __init__(self,department,specialist_setup_model,specialist_preferences_model,specialist_reagent_model):

		self.department= department
		self.specialist_setup_model= apps.get_model(app_label="inventory", model_name= specialist_setup_model)
		self.specialist_preferences_model= apps.get_model(app_label="inventory", model_name= specialist_preferences_model)
		self.specialist_reagent_model= apps.get_model(app_label="inventory", model_name= specialist_reagent_model)


	def send_expiration_email(self):

		all_specialist= self.specialist_setup_model.objects.all()
		specialist_user= None

		for specialist in all_specialist:
			dict_of_attributes= specialist.__dict__
			if dict_of_attributes[self.department] == True:
				specialist_user= specialist

		specialist_email= specialist_user.user.email
		specialist_data= self.specialist_preferences_model.objects.get(specialist=specialist_user.user)
		specialist_alert= specialist_data.alert_for_expiration
		
		reagent_lots= self.specialist_reagent_model.objects.values_list('reagent_lot', flat=True)
		reagent_lot_list= list(reagent_lots)
		
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


hematology= check_expiration("hematology_specialist", "specialist_setup", "specialist_preferences","hematology_inventory")
hematology.send_expiration_email()
chemistry= check_expiration("chemistry_specialist", "specialist_setup", "specialist_preferences","chemistry_inventory")
chemistry.send_expiration_email()
hematology= check_expiration("hematology_specialist", "specialist_setup", "specialist_preferences","hematology_inventory")
hematology.send_expiration_email()
chemistry= check_expiration("chemistry_specialist", "specialist_setup", "specialist_preferences","chemistry_inventory")
chemistry.send_expiration_email()
hematology= check_expiration("hematology_specialist", "specialist_setup", "specialist_preferences","hematology_inventory")
hematology.send_expiration_email()


