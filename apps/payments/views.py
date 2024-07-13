from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy

from apps.payments.filters import SponsorFilter
from apps.payments.forms import ApplicationRegisterForm, ApplicationUpdaterForm, SponsorStudentCreateForm, SponsorStudentUpdateForm
from apps.payments.models import Sponsor, SponsorStudent


class ApplicationRegisterView(CreateView):
    model = Sponsor
    form_class = ApplicationRegisterForm
    template_name = 'application_form.html'
    success_url = reverse_lazy('application')

    def form_valid(self, form):
        messages.success(self.request, 'Application successfully register ')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Sponsor.objects.all()

        self.filterset = SponsorFilter(self.request.GET, queryset=context['objects'])
        context['objects'] = self.filterset.qs
        context['filter'] = self.filterset
            
        return context


class ApplicationDeleteView(DeleteView):
    model = Sponsor
    template_name = 'delete_obj.html'
    success_url = reverse_lazy('application')


class ApplicationUpdateView(UpdateView):
    model = Sponsor
    template_name = 'application_form.html'
    form_class = ApplicationUpdaterForm
    success_url = reverse_lazy('application')


class SponsorStudentCreateView(CreateView):
    model = SponsorStudent
    form_class = SponsorStudentCreateForm
    template_name = 'sponsor_student_form.html'
    success_url = reverse_lazy('sponsor_student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = SponsorStudent.objects.all()

        return context


class SponsorStudentDeleteView(DeleteView):
    model = SponsorStudent
    template_name = 'delete_obj.html'
    success_url = reverse_lazy('sponsor_student')


class SponsorStudentUpdateView(UpdateView):
    model = SponsorStudent
    template_name = 'sponsor_student_form.html'
    form_class = SponsorStudentUpdateForm
    success_url = reverse_lazy('sponsor_student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sp_st'] = SponsorStudent.objects.get(id=self.kwargs['pk'])
        return context