from django.contrib import admin
from structure.models import Structure, Permission, StructurePerm


admin.site.register(Structure)

admin.site.register(Permission)
admin.site.register(StructurePerm)
