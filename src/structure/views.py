from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from franchise.views import franchise
from structure.models import Permission, Structure
from franchise.models import Franchise
from django.db.models import Q # permet de faire une recherche sur plusieurs champs
from structure.forms import AddStructureForm, ChangePerm
from django.contrib import auth, messages



# Create your views here.
def list_structure(request):
    structures = Structure.objects.filter(is_active=True)
    franchises = Franchise.objects.filter(is_active=True)
    print("structures ==>", structures)
    return render(request, 'list_structure.html', context={'structures': structures, 'franchises': franchises,})





def search(request):
    search = request.GET.get('search')
    results_structure = Structure.objects.filter(Q(name__icontains=search) |
                                        Q(address__icontains=search))
    results_franchise = Franchise.objects.filter(name__icontains=search)
    return render(request, 'search.html', context={'results_structure': results_structure, 'results_franchise':results_franchise})



#--------------* ADD STRUCTURE *--------------#

def add_Structure(request):
    form = AddStructureForm()
    if request.method == 'POST':
        form = AddStructureForm(request.POST)
        if form.is_valid():
            franchise = form.save()
            messages.success(request, "Une nouvelle structure vient d'être créé.")
    return render(request, 'add_structure.html', context={'form': form})

  
def structure(request, structure_slug):
    structures = get_object_or_404(Structure, slug=structure_slug)
    # form = ChangePerm()
    # if request.method == "POST":
    #     form = ChangePerm(request.POST)
    #     if form.is_valid():
    #         permission = form.save()
    #         messages.success(request, "Les modification on bien était prise en compte")
    return render(request, 'structure.html', context={'structures': structures})

    



# def structure(request, slug):
#     structures = Structure.objects.get(slug=slug)
#     return render(request, 'structure.html', context={'structures': structures})
    

# def changePermForm(request):
#     form = ChangePerm()
#     if request.method == "POST":
#         form = ChangePerm(request.POST)
#         if form.is_valid():
#             permission = form.save()
#             messages.success(request, "Les modification on bien était prise en compte")
#     return render(request, 'structure.html', context={'form':form})
        # perm = Permission.objects.get()
        # permissions = Structure.objects.filter(permission=perm)
    