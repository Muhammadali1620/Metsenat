from django.urls import path
from . import views


urlpatterns = [
    path('', views.StudentRegisterView.as_view(), name='student_register'),
    path('delete/<int:pk>/student/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('update/<int:pk>/student/', views.StudentUpdateView.as_view(), name='update_student'),
    path('add_university/', views.CreateUniversity.as_view(), name='add_university'),
    path('delete/<int:pk>/university/', views.UniversityDeleteView.as_view(), name='delete_university'),
    path('update/<int:pk>/university/', views.UniversityUpdateView.as_view(), name='update_university'),
]