
from django.db import models
from account.models import User


# Create your models here.
class Franchise(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.name

