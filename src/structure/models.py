from django.urls import reverse
from django.db import models
from account.models import User
from django.utils.text import slugify
from franchise.models import Franchise
from permission.models import Permission





class Structure(models.Model):
    name = models.CharField(max_length=20)
    franchise = models.ForeignKey(Franchise, on_delete = models.SET_NULL, null = True)
    manager = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    permission = models.ManyToManyField(Permission,blank=True, null=True)
    slug = models.SlugField(max_length=20)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="icons/structures", null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
        
    def save(self, *args, **kwargs): #remplissage du slug automatique
        self.slug = slugify(self.name)
        super(Structure, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_structure', args=[self.slug]) 

