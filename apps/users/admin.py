from django.contrib import admin

from apps.users.models import Student, University


@admin.register(Student)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'university', 'level', 'contract', 'sponsored_amount', 'phone_number',]
    list_display_links = list_display


@admin.register(University)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = list_display