
from django.shortcuts import get_object_or_404, render, redirect
from franchise.views import franchise
from structure.models import Structure, slugify
from franchise.models import Franchise
from permission.models import Permission
from account.models import User
from django.db.models import Q 


from structure.forms import AddStructureForm, StructureRequestManagerForm, EditStructureForm
from django.contrib import auth, messages

def test(structure_slug):
    structure = Structure.objects.get(slug=structure_slug)
    permissions = structure.permission
    print(permissions)

#--------------* STRUCTURE DETAIL *--------------#
def structure(request, structure_slug):
    structure = Structure.objects.filter(slug=structure_slug)
    permission = Permission.objects.all()
    structures = get_object_or_404(Structure, slug=structure_slug)
    test(structure_slug)

    return render(request, 'structure.html', context={'structures': structures, 'structure':structure, 'permission': permission})


# --------------* LIST STRUCTURE *--------------#
def list_structure(request):
    structures = Structure.objects.all()
    franchises = Franchise.objects.all()

    return render(request, 'list_structure.html', context={'structures': structures, 'franchises': franchises,})


# --------------* CREATE STRUCTURE *--------------#
def create_structure(request):
    form = AddStructureForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = AddStructureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Une nouvelle structure vient d'être créé.")
            return redirect('list_structure')
    else:
        form = AddStructureForm()
    return render(request, 'formulaires/create_structure.html', context={'form': form})

# -----------* Delete structures *------------#
def delete_structure(request, id):
    form = Structure.objects.get(id=id)
    if request.method =='POST':
        form.delete()
        messages.success(request, "La structure à bien était supprimé.")
        return redirect('list_structure')
    return render(request, 'formulaires/delete_structure.html', context={'form': form})


# --------------* Edit STRUCTURE *--------------#

def edit_structure(request,id):
    structures = Structure.objects.get(id=id)
    form = EditStructureForm(instance=structures)
    if request.method =='POST':
        form = EditStructureForm(request.POST, instance=structures)
        if form.is_valid():
            form.save()
            return redirect('list_structure')
    return render(request, 'formulaires/edit_structure.html', context={'form': form, 'structures':structures})




def StructureRequestManager(request):
    form = StructureRequestManagerForm()
    return render(request, 'structure_request_manager.html')


# --------------* SEARCH BAR *--------------#
def search(request):
    search = request.POST.get('search')
    results_structure = Structure.objects.filter(Q(name__icontains=search) |
                                        Q(address__icontains=search))
    results_franchise = Franchise.objects.filter(name__icontains=search)
    return render(request, 'search.html', context={'results_structure': results_structure, 'results_franchise':results_franchise})






