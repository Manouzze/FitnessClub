from django.shortcuts import get_object_or_404, render
from structure.models import Structure, Structure
from franchise.models import Franchise

# Create your views here.
def list_structure(request):
    structures = Structure.objects.filter(is_active=True)

    return render(request, 'list_structure.html', context={'structures': structures,})


def structure(request, slug):
    structures = Structure.objects.get(slug=slug)
    return render(request, 'structure.html', context={'structures': structures,})