from dataclasses import field
from structure.models import Structure
from django.forms import ModelForm
from permission.models import Permission
from django.db import models
# from django.views.generic import UpdateView
from django import forms

class AddStructureForm(ModelForm):
    class Meta:
        model = Structure
        fields = ('name', 'permission','franchise', 'manager', 'address', 'description', 'is_active', 'image')




class StructureRequestManagerForm(forms.Form):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    new_structure = models.CharField(max_length=100)
    address_structure = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class EditStructureForm(ModelForm):
    class Meta:
        model = Structure
        fields = ('name', 'permission','franchise', 'manager', 'address', 'description', 'is_active')