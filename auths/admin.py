from django.contrib import admin
from auths.models import User, Profile

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['fullname', 'image', 'bio', 'verified']
