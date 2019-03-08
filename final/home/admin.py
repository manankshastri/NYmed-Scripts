from django.contrib import admin
from .models import Patient, Doctor, Prescription, Hospital
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

admin.site.register(User)


class PrecInLine(admin.TabularInline):
    model = Prescription



# define the doctor admin class
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'user', 'first_name', 'last_name', 'email', 'gender', 'specialty', 'hospital')
    fields = ['user', 'ssn', ('first_name', 'last_name', 'email', 'gender'), ('specialty', 'hospital')]
    inlines = [PrecInLine]


# register the admin class with the associated model
admin.site.register(Doctor, DoctorAdmin)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'user', 'first_name', 'last_name','email', 'gender', 'phone')
    fields = ['ssn', ('user', 'first_name', 'last_name','email', 'phone'), 'gender']


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'dop', 'desc')


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'depart')