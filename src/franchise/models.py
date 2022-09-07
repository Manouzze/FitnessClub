
from django.db import models
from account.models import User
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Franchise(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    manager = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs): #remplissage du slug automatique
        self.slug = slugify(self.name)
        super(Franchise, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('franchise', args=[self.slug]) 



