from dataclasses import field
from structure.models import Permission, Structure
from django.forms import ModelForm
from django import forms

class AddStructureForm(ModelForm):
    class Meta:
        model = Structure
        fields = ('name', 'franchise', 'address', 'description', 'is_active', 'permissions')


class ChangePerm(ModelForm):
    class Meta:
        model = Permission
        fields = "__all__"