from django import forms

from Patient import models 


class ConsultationReportForm(forms.Form):
    report = forms.CharField(label='Report', widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Doctor Report Section' }))
    pharmacy = forms.ModelChoiceField(label='Pharmacy', queryset=models.pharmacy.objects.all(), initial=0,widget=forms.Select(attrs={'class':'form-control'}))
    prescription = forms.CharField(label='Prescriptions', widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Please describe drugs prescriptions' }))
    pin = forms.CharField(label='Patient Secret Number', widget=forms.NumberInput(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Secret Pin Provided in SMS' }))
    
