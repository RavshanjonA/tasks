from django.contrib import admin

from base.models import Task

admin.site.site_header = 'Task Admin Dashboard'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'user', 'description', 'created_at', 'complete')
    list_filter = ('complete',)
