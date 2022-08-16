from django.contrib import admin
from structure.models import Structure, Permission


class StrucureAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('name',), }


admin.site.register(Structure, StrucureAdmin)
admin.site.register(Permission)
