from django.urls import path, include
from .views import home, patient, doctor

urlpatterns = [
    path('', home.index, name='index'),

    path('patient/', include(([
        path('pro/', patient.PatientListView.as_view(), name='patient_list'),
        path('pro/profile/<int:pk>', patient.PatientProfileView.as_view(), name='patient_profile'),
        path('pro/<int:pk>', patient.PatientDetailView.as_view(), name='patient_detail'),
        path('pro/profile/<int:pk>/edit/<int:ppk>', patient.PatientProfileUpdateView.as_view(), name='patient_edit'),
    ], 'home'), namespace='patient')),

    path('doctor/', include(([
        path('doc/', doctor.DoctorListView.as_view(), name='doctor_list'),
        path('doc/profile/<int:pk>/', doctor.DoctorProfileView.as_view(), name='doctor_profile'),
        path('doc/<int:pk>/', doctor.DoctorDetailView.as_view(), name='doctor_detail'),
        path('doc/<int:pk>/prescription/add/', doctor.PrescriptionCreateView.as_view(), name='doctor_addpresc'),
        path('doc/<int:pk>/prescription/<int:ppk>/delete/', doctor.PrescriptionDeleteView.as_view(), name='prescription_confirm_delete'),
        path('doc/<int:pk>/prescription/<int:ppk>/edit/', doctor.PrescriptionUpdateView.as_view(), name='prescription_edit'),
    ], 'home'), namespace='doctor')),
]