
from django.shortcuts import get_object_or_404, render, redirect
from franchise.views import franchise
from structure.models import Permission, Structure, slugify
from franchise.models import Franchise
from django.db.models import Q # permet de faire une recherche sur plusieurs champs
from structure.forms import AddStructureForm, UpdatePermission
from django.contrib import auth, messages




#--------------* STRUCTURE DETAIL *--------------#
def structure(request, structure_slug):
    structureperms = Structure.objects.filter(slug=structure_slug)
    structures = get_object_or_404(Structure, slug=structure_slug)
    return render(request, 'structure.html', context={'structures': structures, 'structureperms':structureperms})


# --------------* LIST STRUCTURE *--------------#
def list_structure(request):
    structures = Structure.objects.filter(is_active=True)
    franchises = Franchise.objects.filter(is_active=True)
    return render(request, 'list_structure.html', context={'structures': structures, 'franchises': franchises,})


# --------------* CREATE STRUCTURE *--------------#
def create_structure(request):
    form = AddStructureForm()
    if request.method == 'POST':
        form = AddStructureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Une nouvelle structure vient d'être créé.")
    return render(request, 'formulaires/create_structure.html', context={'form': form})

# -----------* Delete structures *------------#
def delete_structure(request, id):
    form = Structure.objects.get(id=id)
    if request.method =='POST':
        form.delete()
        return redirect('list_structure')
    return render(request, 'formulaires/delete_structure.html', context={'form': form})


# -----------* UPDATE permissions by structure *------------#
def update_permission(request,id):
    structures = get_object_or_404(Structure, id=id)
    form = UpdatePermission(instance=structures)
    if request.method =='POST':
        form = UpdatePermission(request.POST, instance=structures)
        if form.is_valid():
            form.save()
            print('save--->',form)
            messages.success(request, "Sauvegardé !! Un mail automatique vient d'être envoyé au franchisé.")
        
    return render(request, 'formulaires/update_permissions.html', context={'form': form})



# --------------* SEARCH BAR *--------------#
def search(request):
    search = request.GET.get('search')
    results_structure = Structure.objects.filter(Q(name__icontains=search) |
                                        Q(address__icontains=search))
    results_franchise = Franchise.objects.filter(name__icontains=search)
    return render(request, 'search.html', context={'results_structure': results_structure, 'results_franchise':results_franchise})




# --------------* CREATE STRUCTURE *--------------#

# def add_Structure(request):
#     form = AddStructureForm()
#     if request.method == 'POST':
#         form = AddStructureForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Une nouvelle structure vient d'être créé.")
#     return render(request, 'add_structure.html', context={'form': form})


