from franchise.models import Franchise
from django.forms import ModelForm
from django import forms

class AddFranchiseForm(ModelForm):
    class Meta:
        model = Franchise
        fields = ('name', 'description', 'is_active' )
