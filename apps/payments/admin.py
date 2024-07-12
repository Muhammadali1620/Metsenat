from django.contrib import admin

from apps.payments.models import Sponsor, SponsorStudent


@admin.register(Sponsor)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'amount', 'person', 'company_name', 'status', 'payment_type', 'used_amount',]
    list_display_links = list_display


@admin.register(SponsorStudent)
class SponsorStudentUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'sponsor','student','amount',   ]
    list_display_links = list_display
