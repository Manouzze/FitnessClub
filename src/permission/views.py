from django.shortcuts import render
from permission.forms import UpdatePermission, AddPermissionForm
# Create your views here.

from structure.models import Structure, slugify
from franchise.models import Franchise
from permission.models import Permission
from account.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

#--------------* Verification mail *--------------#
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, EmailMessage
from fitnessClub import settings


# -----------* UPDATE permissions by structure *------------#
def update_permission(request,id):
    structures = Structure.objects.get(id=id)
    form = UpdatePermission(instance=structures)
    franchise = Franchise.objects.get(structure=structures)
    print('------------------>', franchise)
    user = User.objects.get(franchise=franchise)
    print('USER ------------------>', user)
    if request.method =='POST':
        form = UpdatePermission(request.POST, instance=structures)
        if form.is_valid():
            form.save()

             # User Activation
            current_site = get_current_site(request)
            mail_subject = 'Confirmation des changements de permissions'
            template = render_to_string('email_confirmation_update_permissions.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=user
            send_email= EmailMessage(mail_subject,template,settings.EMAIL_HOST_USER,[to_email])
            send_email.send()
            messages.success(request, "Sauvegardé !! Un mail automatique vient d'être envoyé au franchisé.")
        
    return render(request, 'update_permissions.html', context={'form': form, 'structures':structures,})


def add_Permission(request):
    form = AddPermissionForm()
    if request.method == 'POST':
        form = AddPermissionForm(request.POST)
        if form.is_valid():
            permission = form.save()
            messages.success(request, "Une nouvelle permission vient d'être créé.")
    return render(request, 'add_permission.html', context={'form': form})


