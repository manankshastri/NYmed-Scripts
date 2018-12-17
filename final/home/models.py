from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    
class Patient(models.Model):
    """model representing patient"""
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)
    email = models.EmailField('Email', max_length=40, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default='M')
    
    class Meta:
        ordering = ['ssn']

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this patient."""
        return reverse('patient_detail', args=[str(self.ssn)])

def create_profile(sender, **kwargs):
    if kwargs['created']:
        patient = Patient.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
    
    

class Hospital(models.Model):
    # for hospital departments
    id = models.IntegerField('ID', primary_key=True)
    depart = models.CharField('Hospital Dept', max_length=25, help_text="Enter the hospital department: ",
                              null=True, blank=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id}'


class Pharmacy(models.Model):
    # for pharmacy info
    id = models.IntegerField('ID', primary_key=True)
    drugid = models.IntegerField('DrugID', blank=False, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.drugid}'

class Doctor(models.Model):
    # model representing doctor
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)
    gender = models.CharField(max_length=3, choices=GENDER_CHOICES, default='M')
    email = models.EmailField('Email', max_length=40, blank=True, null=True, unique=True)
    specialty = models.CharField(max_length=50, default='ENT')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.specialty})'

    class Meta:
        ordering = ['ssn']

    def get_absolute_url(self):
        return reverse('doctor:doctor_detail', args=[str(self.ssn)])

def create_profile_doc(sender, **kwargs):
    if kwargs['created']:
        doctor = Doctor.objects.create(user=kwargs['instance'])

post_save.connect(create_profile_doc, sender=User)

class Prescription(models.Model):
    # model representing prescription
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    dop = models.DateField('Prescription Date', null=True, blank=False)
    desc = models.CharField('Prescription Details', null=True, max_length=150)

    class Meta:
        ordering = ['-dop']

    def __str__(self):
        return f'{self.patient} {self.doctor} {self.desc}'

    def get_absolute_url(self):
        return reverse('doctor:doctor_detail', args=[str(self.doctor.ssn)])
