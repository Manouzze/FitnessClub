
from django.urls import path
from account.views import add_User, logoutUser




urlpatterns = [

    path('logout/', logoutUser, name='logout'),
    path('ajouter/', add_User, name='add_User'),
    
]
