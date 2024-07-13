from django import forms
from apps.payments.models import Sponsor, SponsorStudent


class ApplicationRegisterForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone_number', 'amount', 'person', 'company_name', 'payment_type']


class ApplicationUpdaterForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone_number', 'status', 'amount', 'person', 'company_name', 'payment_type']


class SponsorStudentCreateForm(forms.ModelForm):
    class Meta:
        model = SponsorStudent
        fields = ['sponsor', 'student', 'amount']


class SponsorStudentUpdateForm(forms.ModelForm):
    class Meta:
        model = SponsorStudent
        fields = ['amount']