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
from structure.views import list_structure, search, structure
from fitnessClub import settings
from django.conf.urls.static import static
from dashboard.views import dashboard
from franchise.views import list_franchise
from account.views import account
from franchise.views import franchise


urlpatterns = [

    path('admin/', admin.site.urls),

    path('account/', include("account.urls")),
    path('account/', account, name='account'),

    path('franchise/', include("franchise.urls")),
    path('dashboard/', dashboard, name='dashboard'),
    
    path('structure/<slug:structure_slug>/', structure, name='structure_detail'),
    path('franchise/<slug:franchise_slug>/', franchise, name='franchise'),
    
    path('franchise/', list_franchise, name='list_franchise'),
    path('structure/', list_structure, name='list_structure'),
    path('structure/', include("structure.urls")),

    path('search/', search, name='search'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
