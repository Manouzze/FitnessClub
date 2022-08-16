from django.shortcuts import render
from structure.models import Structure
from franchise.models import Franchise
from account.models import User
from dashboard.forms import AddPermissionForm
from django.contrib import auth, messages

# Create your views here.

def dashboard(request):
    structures = Structure.objects.count()
    franchises = Franchise.objects.count()
    user = User.objects.filter(is_staff=False, is_admin=False)
    users = user.count()
    return render(request, 'dashboard.html', context={'structures':structures, 'franchises':franchises, 'users':users,})



def add_Permission(request):
    form = AddPermissionForm()
    if request.method == 'POST':
        form = AddPermissionForm(request.POST)
        if form.is_valid():
            permission = form.save()
            messages.success(request, "Une nouvelle permission vient d'être créé.")
    return render(request, 'add_permission.html', context={'form': form})