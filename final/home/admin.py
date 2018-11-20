from django.contrib import admin
from .models import Patient, Doctor, Prescription, Hospital, Pharmacy
# Register your models here.


class PrecInLine(admin.TabularInline):
    model = Prescription


# define the doctor admin class
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'first_name', 'last_name', 'specialty', 'hosp_id')
    fields = ['ssn', ('prefix', 'first_name', 'last_name'), ('specialty', 'hosp_id')]
    inlines = [PrecInLine]


# register the admin class with the associated model
admin.site.register(Doctor, DoctorAdmin)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'first_name', 'last_name')
    fields = ['ssn', ('first_name', 'last_name'), 'gender']


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'dop', 'desc', 'drug')


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'depart')


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('id', 'drugid')