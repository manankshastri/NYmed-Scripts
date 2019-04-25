from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView, FormView

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
    
    
@method_decorator([login_required, patient_required], name='dispatch')
class PatientProfileUpdateView(UpdateView):
    model = Patient
    fields = ('email','phone','creditcard',)
    template_name = 'home/patient/patient_edit.html'
    pk_url_kwarg = 'ppk'
    
    def get_queryset(self):
        return Patient.objects.filter(ssn=self.request.user.patient.ssn)
        
    def get_success_url(self):
        return reverse_lazy('patient:patient_profile', kwargs={'pk': self.request.user.patient.ssn})

@method_decorator([login_required, patient_required], name='dispatch')
class PatientBillDetailView(DetailView):
    model = Prescription
    template_name = 'home/patient/patient_bill.html'
    context_object_name = 'prescription'
    pk_url_kwarg = 'ppk'
    
    def get_queryset(self):
        return Prescription.objects.filter(patient = self.request.user.patient)

@method_decorator([login_required, patient_required], name='dispatch')
class PatientBillConfirmUpdateView(UpdateView):
    model = Patient
    fields = ('creditcard',)
    template_name = 'home/patient/patient_confirm_bill.html'
    pk_url_kwarg = 'ppk'
    
    def get_queryset(self):
        return Patient.objects.filter(ssn=self.request.user.patient.ssn)
    
    def get_success_url(self):
        return reverse_lazy('patient:patient_detail', kwargs={'pk': self.request.user.patient.ssn})
    
