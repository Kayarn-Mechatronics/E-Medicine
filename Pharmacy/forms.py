from django import forms

from Patient import models 


class PrescriptionReportForm(forms.Form):
    bill = forms.CharField(label='Amount Charged', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Amount Charged' }))
    pin = forms.CharField(label='Amount Charged', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Secret Pin sent to SMS' }))