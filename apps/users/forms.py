from django import forms
from apps.users.models import Student, University


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'university', 'level', 'contract', 'phone_number']


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'university', 'level', 'phone_number']


class UniversityCreateForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name']
