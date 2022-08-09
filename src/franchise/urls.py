from django.urls import include, path
from franchise.views import add_Franchise

urlpatterns = [
 
  path('ajouter/', add_Franchise, name='add_Franchise'),


    
]