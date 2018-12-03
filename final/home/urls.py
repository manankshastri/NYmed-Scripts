from django.urls import path, include
from .views import home, patient, doctor

urlpatterns = [
    path('', home.index, name='index'),

    path('patient/', include(([
        path('pro/', patient.PatientListView.as_view(), name='patient_list'),
        path('pro/<int:pk>', patient.PatientDetailView.as_view(), name='patient_detail')
    ], 'home'), namespace='patient')),

    path('doctor/', include(([
        path('doc/', doctor.DoctorListView.as_view(), name='doctor_list'),
        path('doc/profile/<int:pk>', doctor.DoctorProfileView.as_view(), name='doctor_profile'),
        path('doc/<int:pk>', doctor.DoctorDetailView.as_view(), name='doctor_detail'),
    ], 'home'), namespace='doctor')),
]