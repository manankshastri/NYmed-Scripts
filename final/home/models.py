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
    email = models.EmailField('Email', max_length=255, blank=True, null=True, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    class Meta:
        ordering = ['ssn']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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
    PREFIX = [('Dr', 'Dr')]
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ssn = models.IntegerField('SSN', blank=False, primary_key=True)
    prefix = models.CharField(max_length=2, choices=PREFIX)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField('Email', max_length=255, blank=True, null=True, unique=True)
    specialty = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.prefix} {self.first_name} {self.last_name} ({self.specialty})'

    class Meta:
        ordering = ['ssn']

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[str(self.ssn)])

def create_profile_doc(sender, **kwargs):
    if kwargs['created']:
        doctor = Doctor.objects.create(user=kwargs['instance'])

post_save.connect(create_profile_doc, sender=User)

class Prescription(models.Model):
    # model representing prescription
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    dop = models.DateField(null=True, blank=False)
    desc = models.TextField('Prescription', help_text='Enter the prescription : ', null=True)

    class Meta:
        ordering = ['patient']

    def __str__(self):
        return f'{self.patient} {self.doctor} {self.desc}'


