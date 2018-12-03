from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from ..decorators import patient_required
from ..forms import PatientSignUpForm
from ..models import Patient, User, Prescription


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient:patient_list')


@method_decorator([login_required, patient_required], name='dispatch')
class PatientListView(ListView):
    model = Patient
    template_name = 'home/patient/patient_list.html'

    def get_queryset(self):
        return Patient.objects.all()


@method_decorator([login_required, patient_required], name='dispatch')
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'home/patient/patient_detail.html'


@method_decorator([login_required, patient_required], name='dispatch')
class PatientProfileView(DetailView):
    model = Patient
    template_name = 'home/patient/patient_profile.html'




