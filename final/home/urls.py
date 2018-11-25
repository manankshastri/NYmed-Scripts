from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('patient_prescription/', views.PatientDetailView.as_view(), name='patient_prescription'),
]