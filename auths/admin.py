from django.contrib import admin
from auths.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['username', 'email', 'bio', 'verified']
