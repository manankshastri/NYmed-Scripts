from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    # path('patient_prescription/', views.PatientDetailView.as_view(), name='patient_prescription'),
    path('p/', views.PatientView.as_view(), name='patients'),
    path('p/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
]