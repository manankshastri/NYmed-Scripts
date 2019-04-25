from django.urls import path, include
from .views import home, patient, doctor, pharmacist

urlpatterns = [
    path('', home.index, name='index'),

    path('patient/', include(([
        path('pro/', patient.PatientListView.as_view(), name='patient_list'),
        path('pro/profile/<int:pk>', patient.PatientProfileView.as_view(), name='patient_profile'),
        path('pro/<int:pk>', patient.PatientDetailView.as_view(), name='patient_detail'),
        path('pro/profile/<int:pk>/edit/<int:ppk>', patient.PatientProfileUpdateView.as_view(), name='patient_edit'),
        path('pro/profile/<int:pk>/viewbill/<int:ppk>', patient.PatientBillDetailView.as_view(), name='patient_bill'),
        path('pro/profile/<int:pk>/viewbill/<int:ppk>/confirmbill', patient.PatientBillConfirmUpdateView.as_view(), name='patient_confirm_bill'),
    ], 'home'), namespace='patient')),

    path('doctor/', include(([
        path('doc/', doctor.DoctorListView.as_view(), name='doctor_list'),
        path('doc/profile/<int:pk>/', doctor.DoctorProfileView.as_view(), name='doctor_profile'),
        path('doc/<int:pk>/', doctor.DoctorDetailView.as_view(), name='doctor_detail'),
        path('doc/<int:pk>/prescription/add/', doctor.PrescriptionCreateView.as_view(), name='doctor_addpresc'),
        path('doc/<int:pk>/prescription/<int:ppk>/delete/', doctor.PrescriptionDeleteView.as_view(), name='prescription_confirm_delete'),
        path('doc/<int:pk>/prescription/<int:ppk>/edit/', doctor.PrescriptionUpdateView.as_view(), name='prescription_edit'),
    ], 'home'), namespace='doctor')),
    
    
    path('pharmacist/', include(([
        path('pha/', pharmacist.PharmacistListView.as_view(), name='pharmacist_list'),
        path('pha/profile/<int:pk>/', pharmacist.PharmacistProfileView.as_view(), name='pharmacist_profile'),
        path('pha/<int:pk>/', pharmacist.PharmacistDetailView, name='pharmacist_detail'),
    ], 'home'), namespace='pharmacist')),
    
]