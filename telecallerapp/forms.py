from django import forms

class LeadUploadForm(forms.Form):
    excel_file = forms.FileField()
