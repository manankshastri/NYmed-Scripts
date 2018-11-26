from django.shortcuts import render
from .models import Patient, Doctor, Prescription
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    """ view function for home page"""

    # generate number of patients
    num_patients = Patient.objects.all().count()

    # generate number of doctors
    num_doctors = Doctor.objects.all().count()

    context = {
        'num_patients': num_patients,
        'num_doctors': num_doctors,
    }

    # render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def about(request):
    """ view function for home page"""
    # generate number of patients
    num_patients = Patient.objects.all().count()

    # generate number of doctors
    num_doctors = Doctor.objects.all().count()

    context = {
        'num_patients': num_patients,
        'num_doctors': num_doctors,
    }

    # render the HTML template index.html with the data in the context variable
    return render(request, 'about.html', context=context)


class PatientView(LoginRequiredMixin, generic.ListView):
    model = Patient
    template_name = 'catalog/patient_list.html'


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient
    template_name = 'catalog/patient_detail.html'


