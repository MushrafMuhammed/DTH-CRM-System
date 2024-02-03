from django import forms
from .models import Telecaller

class LeadAssignForm(forms.Form):
    telecaller = forms.ModelChoiceField(queryset=Telecaller.objects.all(), empty_label="Select", required=True)
    start = forms.IntegerField(min_value=1, required=True)
    end = forms.IntegerField(min_value=1, required=True)
    