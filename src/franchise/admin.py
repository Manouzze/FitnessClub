from django.contrib import admin

from franchise.models import Franchise



class FranchiseAdmin(admin.ModelAdmin):
  prepopulated_fields: {'slug':('name')}


admin.site.register(Franchise, FranchiseAdmin)