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
from structure.views import list_structure, search
# from fitnessClub import settings
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import dashboard
from franchise.views import list_franchise
from account.views import account
from franchise.views import franchise


urlpatterns = [

    path('admin/', admin.site.urls),

    path('dashboard/', include("dashboard.urls")),
    path('account/', include("account.urls")),
    path('franchise/', include("franchise.urls")),
    path('structure/', include("structure.urls")),

    path('account/', account, name='account'),
    path('dashboard/', dashboard, name='dashboard'),
    
    path('franchise/<slug:franchise_slug>/', franchise, name='franchise'),

    
    path('franchise/', list_franchise, name='list_franchise'),
    path('structure/', list_structure, name='list_structure'),

    path('search/', search, name='search'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
