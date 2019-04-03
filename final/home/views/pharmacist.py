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

from ..decorators import pharmacist_required
from ..forms import PharmacistSignUpForm
from ..models import Pharmacist, User, Prescription


class PharmacistSignUpView(CreateView):
    model = User
    form_class = PharmacistSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'pharmacist'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pharmacist:pharmacist_list')
    
    
@login_required
@pharmacist_required
def PharmacistDetailView(request, pk):
    pres_all = Prescription.objects.all()
    template_name = 'home/pharmacist/pharmacist_detail.html'
    
    return render(request, template_name, context={'pres_all': pres_all},)


@method_decorator([login_required, pharmacist_required], name='dispatch')
class PharmacistListView(ListView):
    model = Pharmacist
    template_name = 'home/pharmacist/pharmacist_list.html'
    

@method_decorator([login_required, pharmacist_required], name='dispatch')
class PharmacistProfileView(DetailView):
    model = Pharmacist
    template_name = 'home/pharmacist/pharmacist_profile.html'