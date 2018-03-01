from django.contrib import admin
from .models import staff, department, designation
# Register your models here.

admin.site.register(staff)
admin.site.register(department)
admin.site.register(designation)