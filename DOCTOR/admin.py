from django.contrib import admin

# Register your models here.
from DOCTOR.models import *
admin.site.register(Doctor)
admin.site.register(Prescription2)
