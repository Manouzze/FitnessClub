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
from django.contrib.auth.decorators import login_required


#--------------* Verification mail *--------------#
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMessage
from fitnessClub import settings



#--------------* Views allowed for staff *--------------#

#--------------* ADD USER *--------------#

def add_User(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            is_staff = form.cleaned_data['is_staff']
            avatar = request.FILES['avatar']
            user = form.save()

            # User Activation
            current_site = get_current_site(request)
            mail_subject = 'Veuillez activer votre compte'
            template = render_to_string('account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email= EmailMessage(mail_subject,template,settings.EMAIL_HOST_USER,[to_email])
            send_email.send()
            messages.success(request, "Un nouveau profile vient d'être créé. Un mail vient de lui être env")

    return render(request, 'ajouter.html', context={'form': form})



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
@login_required(login_url='login')
def logoutUser(request):
    auth.logout(request)
    messages.success(request, 'Vous êtes déconnecté')
    return redirect('login')


#--------------* ACCOUNT *--------------#

def account(request):
    current_user = request.user
    franchises = Franchise.objects.filter(manager=current_user)
    structures = Structure.objects.filter(manager=current_user)
    return render(request, 'account.html', context={'franchises': franchises, 'structures': structures, })






#--------------* Activer *--------------#

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('login')