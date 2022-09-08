from django.urls import include, path
from franchise.views import add_Franchise, edit_franchise

urlpatterns = [
 
  path('edit/<int:id>/', edit_franchise, name='edit_franchise'),
  path('ajouter/', add_Franchise, name='add_Franchise'),




    
]