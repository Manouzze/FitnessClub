from django.shortcuts import render
from franchise.models import Franchise
from structure.models import Structure

# Create your views here.
def list_franchise(request):
    franchises = Franchise.objects.filter(is_active=True)
    return render(request, 'list_franchise.html', context={'franchises': franchises,})

def franchise(request, slug):
    franchises = Franchise.objects.get(slug=slug)
    structures = Structure.objects.filter(is_active=True)
    return render(request, 'franchise.html', context={'franchises': franchises, 'structures': structures,})