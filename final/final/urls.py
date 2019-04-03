"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from home.views import home, patient, doctor, pharmacist
# from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    # path('', RedirectView.as_view(url='/home/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', home.SignUpView.as_view(), name='signup'),
    path('accounts/signup/patient/', patient.PatientSignUpView.as_view(), name='patient_signup'),
    path('accounts/signup/doctor/', doctor.DoctorSignUpView.as_view(), name='doctor_signup'),
    path('accounts/signup/pharmacist/', pharmacist.PharmacistSignUpView.as_view(), name='pharmacist_signup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


