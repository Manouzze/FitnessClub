from django.shortcuts import render
from structure.models import Structure
from franchise.models import Franchise
from account.models import User
from django.contrib import auth, messages

# Create your views here.

def dashboard(request):
    structures = Structure.objects.count()
    franchises = Franchise.objects.count()
    user = User.objects.filter(is_staff=False, is_admin=False)
    users = user.count()
    return render(request, 'dashboard.html', context={'structures':structures, 'franchises':franchises, 'users':users,})



