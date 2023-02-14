from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_filter = ('id', 'title', 'created_at')
    search_fields = ('title', 'created_at')
    fields = ('date', 'title', 'created_at')
    readonly_fields = ('id', 'created_at')

admin.site.register(Task, TaskAdmin)