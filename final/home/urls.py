from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p/', views.PatientView.as_view(), name='patients'),
    path('p/<int:pk>', views.PatientDetailView.as_view(), name='patient-detail'),
]