from structure.models import Permission
from django.forms import ModelForm
from django import forms

class AddPermissionForm(ModelForm):
    class Meta:
        model = Permission
        fields = ('name', 'is_active',)