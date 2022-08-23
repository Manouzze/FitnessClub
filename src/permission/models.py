from django.db import models

# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=20, null=True)
    icon = models.ImageField(upload_to="icons/permissions", blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)