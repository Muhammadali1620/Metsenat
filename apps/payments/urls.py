from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationRegisterView.as_view(), name='application'),
    path('delete/<int:pk>/application/', views.ApplicationDeleteView.as_view(), name='delete_application'),
    path('update/<int:pk>/application/', views.ApplicationUpdateView.as_view(), name='update_application'),

    path('sponsor_student/', views.SponsorStudentCreateView.as_view(), name='sponsor_student'),
    path('delete/<int:pk>/sponsor_student/', views.SponsorStudentDeleteView.as_view(), name='delete_sponsor_student'),
    path('update/<int:pk>/sponsor_student/', views.SponsorStudentUpdateView.as_view(), name='update_sponsor_student'),
]