from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from home.models import (User, Patient, Doctor, Pharmacist)


class DoctorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        return user


class PatientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        
    @transaction.atomic    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user
    

class PharmacistSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )
        
    @transaction.atomic    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_pharmacist = True
        if commit:
            user.save()
        return user