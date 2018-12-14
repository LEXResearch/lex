from django.contrib import admin

from .models import Subject, LeadModel, LeadGerated

admin.site.register(Subject)
admin.site.register(LeadModel)
admin.site.register(LeadGerated)
