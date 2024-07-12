from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from apps.users.filters import StudentFilter
from apps.users.forms import StudentRegisterForm, UniversityCreateForm
from apps.users.models import Student, University


class StudentRegisterView(CreateView):
    model = Student
    form_class = StudentRegisterForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_register')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Student.objects.all()

        self.filterset = StudentFilter(self.request.GET, queryset=context['objects'])
        context['objects'] = self.filterset.qs
        context['filter'] = self.filterset

        return context


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'delete_obj.html'
    success_url = reverse_lazy('student_register')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    form_class = StudentRegisterForm
    success_url = reverse_lazy('student_register')


class CreateUniversity(CreateView):
    model = University
    form_class = UniversityCreateForm
    template_name = 'university_form.html'
    success_url = reverse_lazy('add_university')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = University.objects.all()

        return context
    

class UniversityDeleteView(DeleteView):
    model = University
    template_name = 'delete_obj.html'
    success_url = reverse_lazy('add_university')


class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'university_form.html'
    form_class = UniversityCreateForm
    success_url = reverse_lazy('add_university')