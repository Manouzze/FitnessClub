from django.shortcuts import get_object_or_404, render
from franchise.models import Franchise
from structure.models import Structure
from franchise.forms import AddFranchiseForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth, messages

# Create your views here.
def list_franchise(request):
    franchises = Franchise.objects.all()
    structures = Structure.objects.filter(is_active=True)
    return render(request, 'list_franchise.html', context={'franchises': franchises, 'structures':structures,})

#--------------* details FRANCHISE *--------------#
def franchise(request, franchise_slug):
    franchises = get_object_or_404(Franchise, slug=franchise_slug)
    structures = Structure.objects.filter(franchise=franchises)
    return render(request, 'franchise.html', context={'franchises': franchises, 'structures': structures,})


def search(request):
    search = request.GET.get('search')
    results_franchise = Franchise.objects.filter(name__icontains=search)
    return render(request, 'search.html', context={'results_franchise':results_franchise})


#--------------* ADD FRANCHISE *--------------#

def add_Franchise(request):
    form = AddFranchiseForm()
    if request.method == 'POST':
        form = AddFranchiseForm(request.POST)
        if form.is_valid():
            franchise = form.save()
            messages.success(request, "Une nouvelle franchise vient d'être créé.")
    return render(request, 'add_franchise.html', context={'form': form})

