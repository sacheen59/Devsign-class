from django.contrib import admin
from api.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task','is_completed','created_at','updated_at']
    list_editable = ['is_completed']
    list_filter = ['created_at']
    # prepopulated_fields = {'slug': ['task',]}

