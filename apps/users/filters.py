import django_filters
from .models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['university', 'level']

# class TeacherFilter(django_filters.FilterSet):
#     class Meta:
#         model = CustomUser
#         fields = ['gender', 'subject']