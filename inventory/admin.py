from django.contrib import admin
from .models import hematology_inventory, chemistry_inventory, historical_hematology_inventory, historical_chemistry_inventory, specialist_preferences

admin.site.register(hematology_inventory)
admin.site.register(chemistry_inventory)
admin.site.register(historical_hematology_inventory)
admin.site.register(historical_chemistry_inventory)


class specialist_preferences_admin(admin.ModelAdmin):
	exclude= ("specialist",)

admin.site.register(specialist_preferences,specialist_preferences_admin)
# admin.site.register(hematology_user_data)