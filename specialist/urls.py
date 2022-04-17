from django.urls import path
from . import views

urlpatterns = [

    path('specialist_preferences', views.get_specialist_preferences, name="specialist_preferences"),   
    path('display_tech_usage', views.display_tech_usage, name="display_tech_usage"), 
    path('tech_usage', views.tech_usage, name="tech_usage"), 
    path('specialist_information', views.home_page_specialist, name="specialist_information"),
    path('modify', views.modify, name="modify"),
    path('add_to_inventory', views.add_to_inventory, name="add_to_inventory"),
    path('reagent_usage', views.historical_usage, name="historical_usage")
]