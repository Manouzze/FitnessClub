import email
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from account.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from franchise.models import Franchise
from franchise.views import franchise
from structure.models import Structure
from . import forms




#--------------* Views allowed for staff *--------------#

#--------------* ADD USER *--------------#

def add_User(request):
    formsignup = forms.SignupForm()
    if request.method == 'POST':
        formsignup = forms.SignupForm(request.POST)
        if formsignup.is_valid():
            user = formsignup.save()
            messages.success(request, "Un nouveau profile vient d'être créé.")
    return render(request, 'ajouter.html', context={'formsignup': formsignup})



#--------------* LOGIN *--------------#

def loginUser(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('account')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'login.html', context={'form': form, 'message': message})

#--------------* LOGOUT *--------------#

def logoutUser(request):
    auth.logout(request)
    messages.success(request, 'Vous êtes déconnecté')
    return redirect('login')


#--------------* ACCOUNT *--------------#

def account(request):
    current_user = request.user
    franchises = Franchise.objects.filter(user=current_user)
    structures = Structure.objects.all()
    return render(request, 'account.html', context={'franchises': franchises, 'structures': structures, })

