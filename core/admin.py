from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_editable = ['is_done']
    list_display = ['title', 'user', 'created_at', 'is_done']
