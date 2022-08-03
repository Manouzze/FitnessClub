import imp
from django.contrib import admin
from django.urls import include, path
from account.views import loginUser, account, add_franchise, logoutUser
from fitnessClub import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('account/', account, name='account'),
    path('add_franchise/', add_franchise, name='add_franchise'),

]
