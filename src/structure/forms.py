from dataclasses import field
from structure.models import Structure
from django.forms import ModelForm
# from django.views.generic import UpdateView
from django import forms

class AddStructureForm(ModelForm):
    class Meta:
        model = Structure
        fields = ('name', 'permission','franchise', 'address', 'description', 'is_active')


class UpdatePermission(ModelForm):
    class Meta:
        model = Structure
        fields = ('permission', 'is_active')
        widgets={
            'permission': forms.CheckboxSelectMultiple(attrs={'class':''})
        }