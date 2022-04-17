from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home_page, name='home_page'),
    path('tech_information_hub', views.tech_information_hub, name="tech_information_hub")
]