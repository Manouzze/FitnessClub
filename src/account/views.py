import email
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from account.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from franchise.models import Franchise
from structure.models import Structure
from . import forms



#--------------* Views allowed for staff *--------------#

#--------------* ADD FRANCHISE *--------------#

def add_franchise(request):
    formsignup = forms.SignupForm()
    if request.method == 'POST':
        formsignup = forms.SignupForm(request.POST)
        if formsignup.is_valid():
            user = formsignup.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'add_franchise.html', context={'formsignup': formsignup})



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
    structures = Structure.objects.filter(is_active=True)
    return render(request, 'account.html', context={'structures': structures,})



