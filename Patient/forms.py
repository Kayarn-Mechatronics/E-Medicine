from secrets import choice
from tkinter import Widget
from django import forms
from django.utils import timezone
from . import models
import datetime




class ConsultationForm(forms.Form):
    datetime = forms.DateTimeField(label='Date', widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}))
    clinic = forms.ModelChoiceField(label='Hospital', queryset=models.clinics.objects.all(), initial=0, widget=forms.Select(attrs={'class': 'form-control', 'id':'gate'}))
    Description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Please describe symptoms or situation' }))

class loginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'email', 'type':'email'}), required=True) 
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'}), required=True)
    remember_me = forms.BooleanField(label='Remember me', widget=forms.CheckboxInput(attrs={'class': 'icheck-primary', 'id':'remember', 'type':'checkbox'}))
