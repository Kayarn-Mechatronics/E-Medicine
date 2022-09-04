from secrets import choice
from django import forms
from django.utils import timezone
from .models import *
import datetime


CLINICS_CHOICES =(
    ("KFWH","KING FAISAL HOSPITAL"),
    ("CRD","LA CROIX DU SUD"),
    ("LC","LEGACY CLINIC"),
    ("C.H.U.K", "C.H.U.K"),
    ("C.H.U.B", "C.H.U.B"),
)


class ConsultationForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}))
    time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time', 'id':'time', 'placeholder':'Time'}))
    clinic = forms.TypedChoiceField(label='Clinic', choices=CLINICS_CHOICES, coerce=str, widget=forms.Select(attrs={'class': 'form-control', 'id':'clinic'}))
    Description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Please describe symptoms or situation' }))

class loginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}), required=True) 
    passowrd = forms.CharField(label='Password', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}), required=True)

