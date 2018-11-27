from django.urls import path, include
from .views import home, patient, doctor

urlpatterns = [
    path('', home.index, name='index'),
    # path('p/', patient.PatientView.as_view(), name='patients'),
    path('patient/<int:pk>', patient.PatientDetailView.as_view(), name='patient-detail'),
    path('doctor/<int:pk>', doctor.DoctorDetailView.as_view(), name='doctor-detail'),
]