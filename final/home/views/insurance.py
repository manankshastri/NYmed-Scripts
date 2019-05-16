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

from ..decorators import insurance_required
from ..forms import InsuranceSignUpForm
from ..models import Insurance, User, Prescription, Patient


class InsuranceSignUpView(CreateView):
    model = User
    form_class = InsuranceSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'insurance'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('insurance:insurance_list')
    
@login_required
@insurance_required
def InsuranceDetailView(request, pk):
    pat_all = Patient.objects.all()
    template_name = 'home/insurance/insurance_detail.html'
    
    return render(request, template_name, context = {'pat_all': pat_all},)


@method_decorator([login_required, insurance_required], name='dispatch')
class InsuranceListView(ListView):
    model = Insurance
    template_name = 'home/insurance/insurance_list.html'
    
@login_required
@insurance_required
def InsurancePatientBillsView(request, pk):
    pat_all = Prescription.objects.all()
    template_name = 'home/insurance/insurance_patient.html'
    
    return render(request, template_name, context = {'pat_all': pat_all},)

@method_decorator([login_required, insurance_required], name='dispatch')
class InsuranceBillDetailView(DetailView):
    model = Prescription
    template_name = 'home/insurance/insurance_bills.html'

