from django.shortcuts import render, HttpResponse
from structure.models import Structure
from franchise.models import Franchise
from account.models import User
from django.contrib import auth, messages
from django.db.models import Q # permet de faire une recherche sur plusieurs champs
from django.http import JsonResponse

# Create your views here.

def dashboard(request):
    search_structure = Structure.objects.all()
    manager_structures = Structure.objects.all()
    structures = Structure.objects.count()
    manager_franchises = Franchise.objects.all()
    franchises = Franchise.objects.count()
    user = User.objects.filter(is_staff=False, is_admin=False)
    users = user.count()
    return render(request, 'dashboard.html', context={'search_structure':search_structure, 'structures':structures, 'franchises':franchises, 'users':users, 'manager_structures':manager_structures, 'manager_franchises':manager_franchises })




# --------------* SEARCH BAR *--------------#
def search(request):
    search = request.POST.get('search')
    results_structure = Structure.objects.filter(Q(name__icontains=search) |
                                        Q(address__icontains=search))
    results_franchise = Franchise.objects.filter(name__icontains=search)
    return render(request, 'search.html', context={'results_structure': results_structure, 'results_franchise':results_franchise})




