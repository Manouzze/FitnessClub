from django.urls import include, path
from dashboard.views import add_Permission

urlpatterns = [
 
  path('ajouter/permission/', add_Permission, name='add_Permission'),

]