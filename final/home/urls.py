from django.urls import path, include
from .views import home, patient, doctor

urlpatterns = [
    path('', home.index, name='index'),
    # path('p/', patient.PatientView.as_view(), name='patients'),
    # path('p/<int:pk>', patient.PatientDetailView.as_view(), name='patient-detail'),

    path('patient/', include(([
        path('<int:pk>/', patient.PatientDetailView.as_view(), name='patient-detail'),
        path('<int:pk>/presc/', patient.PatientPrescriptionView.as_view(), name='patient-presc'),
    ], 'home'), namespace='patients')),

    """
    path('doctor/', include(([
        path('', )
    ])))
    """
]