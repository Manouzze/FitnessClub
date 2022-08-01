"""fitnessClub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import include, path
from account.views import loginUser, account, add_franchise, logoutUser, base
from structure.views import list_structure, structure
from fitnessClub import settings
from django.conf.urls.static import static
from franchise.views import list_franchise


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base),
    path('list_structure/', list_structure, name='list_structure'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('account/', account, name='account'),
    path('add_franchise/', add_franchise, name='add_franchise'),
    path('list_franchise/', list_franchise, name='list_franchise'),
    path('structure/<str:slug>/', structure, name='structure'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
