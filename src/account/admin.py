from django.contrib import admin
from account.models import User

class UserAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'is_active', 'is_staff', 'is_admin')

admin.site.register(User, UserAdmin)