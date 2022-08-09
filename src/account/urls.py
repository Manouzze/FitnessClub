
from django.urls import path
from account.views import loginUser, add_User, logoutUser




urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('ajouter/', add_User, name='add_User'),
    
]
