from django.forms import ModelForm
from structure.models import Structure
from django import forms
from permission.models import Permission

class UpdatePermission(ModelForm):
    class Meta:
        model = Structure
        fields = ('permission', 'is_active')



class AddPermissionForm(ModelForm):
    class Meta:
        model = Permission
        fields = ('name', 'is_active','icon')