from django.urls import include, path
from franchise.views import add_Franchise, search

urlpatterns = [
 
  path('ajouter/', add_Franchise, name='add_Franchise'),
  path('search/', search, name='search-franchise'),



    
]