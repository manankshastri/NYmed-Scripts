from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, ListView, DeleteView, DetailView, UpdateView)
from django.contrib.messages.views import SuccessMessageMixin

from ..decorators import doctor_required
from ..forms import DoctorSignUpForm
from ..models import Doctor, User, Prescription


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor:doctor_list')


@method_decorator([login_required, doctor_required], name='dispatch')
class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'home/doctor/doctor_detail.html'


@method_decorator([login_required, doctor_required], name='dispatch')
class DoctorListView(ListView):
    model = Doctor
    template_name = 'home/doctor/doctor_list.html'

    
@method_decorator([login_required, doctor_required], name='dispatch')
class DoctorProfileView(DetailView):
    model = Doctor
    template_name = 'home/doctor/doctor_profile.html'
    

@method_decorator([login_required, doctor_required], name='dispatch')
class PrescriptionCreateView(CreateView):
    model = Prescription
    fields = ('patient', 'dop', 'desc', )
    template_name = 'home/doctor/doctor_addpresc.html'

    
    def form_valid(self, form):
        form.instance.doctor = self.request.user.doctor
        return super().form_valid(form)


    
@method_decorator([login_required, doctor_required], name='dispatch')
class PrescriptionDeleteView(DeleteView):
    model = Prescription
    context_object_name = 'prescription'
    template_name = 'home/doctor/prescription_confirm_delete.html'
    pk_url_kwarg = 'ppk'
    
    def delete(self, request, *args, **kwargs):
        prescription = self.get_object()
        messages.success(request, 'The prescription of "%s" was deleted with success!' % prescription.patient)
        return super().delete(request, *args, **kwargs)
    
    def get_queryset(self):
        return Prescription.objects.filter(doctor = self.request.user.doctor)
    
    def get_success_url(self):
        doc = self.object.doctor
        return reverse_lazy('doctor:doctor_detail', kwargs={'pk': doc.ssn})
    
@method_decorator([login_required, doctor_required], name='dispatch')
class PrescriptionUpdateView(UpdateView):
    model = Prescription
    fields = ('dop', 'desc',)
    context_object_name = 'prescription'
    template_name = 'home/doctor/prescription_edit.html'
    pk_url_kwarg = 'ppk'
    
    def get_queryset(self):
        return Prescription.objects.filter(doctor = self.request.user.doctor)
    
    def get_success_url(self):
        doc = self.object.doctor
        return reverse_lazy('doctor:doctor_detail', kwargs={'pk': doc.ssn})