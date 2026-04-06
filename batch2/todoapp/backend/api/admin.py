from django.contrib import admin
from api.models import Task,CustomUser

# Register your models here.

admin.site.register(CustomUser)
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task','created_at','updated_at']
    list_filter = ['created_at']
    # prepopulated_fields = {'slug': ['task',]}

