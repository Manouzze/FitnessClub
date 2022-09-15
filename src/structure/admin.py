from django.contrib import admin
from structure.models import Structure




class StrucureAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',), }


admin.site.register(Structure, StrucureAdmin)

