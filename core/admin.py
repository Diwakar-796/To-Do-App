from django.contrib import admin
from .models import Task, Category, Donation

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_editable = ['level', 'is_done']
    list_display = ['title', 'user', 'level', 'created_at', 'is_done']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_editable = ['status']
    list_display = ['did', 'user', 'status', 'date']
