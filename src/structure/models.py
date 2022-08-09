from django.urls import reverse
from django.db import models
from account.models import User

from franchise.models import Franchise



class Permission(models.Model):
    name = models.CharField(max_length=20, null=True)
    mailling = models.BooleanField(default=True)
    planning = models.BooleanField(default=True)
    promotion = models.BooleanField(default=True)
    smoothie = models.BooleanField(default=False)
    distributer = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    statistic = models.BooleanField(default=False)
    coaching = models.BooleanField(default=True)
    shower = models.BooleanField(default=True)
    entretien = models.BooleanField(default=False)
    proteine = models.BooleanField(default=True)
    massage = models.BooleanField(default=False)
    evenement = models.BooleanField(default=False)
    concours = models.BooleanField(default=False)
    nettoyage = models.BooleanField(default=False)
    assurance = models.BooleanField(default=False)
    def __str__(self):
        return str(self.name)

class Structure(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    franchise = models.ForeignKey(Franchise, on_delete = models.SET_NULL, null = True)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    permissions = models.ForeignKey(Permission, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="icons/structures", null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('structure_detail', args=[self.slug]) 


class StructurePerm(models.Model):
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.structure)
