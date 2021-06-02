from django.contrib import admin

from base.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title', 'user')
    list_display = ('title', 'user', 'description', 'complete', 'created_at')
    list_filter = ('complete',)
