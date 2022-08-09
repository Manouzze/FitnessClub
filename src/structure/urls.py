
from django.urls import include, path
from structure.views import structure, add_Structure



urlpatterns = [
  
    path('ajouter/', add_Structure, name='add_Structure'),

    
]
