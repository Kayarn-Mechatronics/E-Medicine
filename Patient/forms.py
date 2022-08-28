from django import forms
from django.utils import timezone
from .models import *
import datetime


class ConsultationForm(forms.Form):
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}))
    time = forms.TimeField(label='Time', widget=forms.TimeInput(attrs={'class': 'form-control', 'type':'time', 'id':'time', 'placeholder':'Time'}))
        