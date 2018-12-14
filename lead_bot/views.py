from django.shortcuts import render

# Create your views here.
from .models import LeadModel, LeadGerated, Subject

# Create your views here.
def lead_view(request):
    leads = LeadGerated.objects.all()
    return render(request, 'lead_view.html', { 'leads': leads})
