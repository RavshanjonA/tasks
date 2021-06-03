from django.contrib import admin

from base.models import Task

admin.site.site_header = 'Task Admin Dashboard'
admin.site.index_title = 'Task Member Adminstrations'
admin.site.site_title = 'Log in'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'user', 'description', 'created_at', 'complete')
    list_filter = ('complete',)
