from django import forms
from . import models
import datetime


Roles = [
		('Patient', 'Patient'),
		('Clinic', 'Clinic'),
		('Pharmacist', 'Pharmacist')]


class registrationForm(forms.Form):
    first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'first_name','placeholder':'First Name'}))
    last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'last_name','placeholder':'Last Name'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email', 'data-inputmask' : '"alias": "email"'}))
    phone = forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class':'form-control', 'id':'phonenum','placeholder':'Phone Number'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','id':'address','placeholder':'Address'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class':'form-control','id':'city','placeholder':'City'}))
    id_number = forms.CharField(label='ID Number', widget=forms.TextInput(attrs={'class':'form-control','id':'idnumber','placeholder':'Identification Number'}))
    dob = forms.CharField(label='Date of Birth', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date','id':'dob'}))
    is_relative = forms.BooleanField(label='I am a relative of Cimerwa Staff', widget=forms.CheckboxInput(attrs={'class':'form-control', 'type':'checkbox','id':'flexSwitchCheckDefault'}))
    

class clinic_registrationForm(forms.Form):
    clinic = forms.CharField(label="Clinic Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'Clinic','placeholder':'Clinic Name'}))
    first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'first_name','placeholder':'First Name'}))
    last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'last_name','placeholder':'Last Name'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email', 'data-inputmask' : '"alias": "email"'}))
    phone = forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class':'form-control', 'id':'phonenum','placeholder':'Phone Number'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','id':'address','placeholder':'Address'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class':'form-control','id':'city','placeholder':'City'}))
    
class pharmacy_registrationForm(forms.Form):
    pharmacy = forms.CharField(label="Pharmacy Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'Pharmacy','placeholder':'Pharmacy'}))
    first_name = forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'first_name','placeholder':'First Name'}))
    last_name = forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control', 'id':'last_name','placeholder':'Last Name'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control','id':'email','placeholder':'Email', 'data-inputmask' : '"alias": "email"'}))
    phone = forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class':'form-control', 'id':'phonenum','placeholder':'Phone Number'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    password_confirmation = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder':'Password'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class':'form-control','id':'address','placeholder':'Address'}))
    city = forms.CharField(label='City', widget=forms.TextInput(attrs={'class':'form-control','id':'city','placeholder':'City'}))

class ConsultationForm(forms.Form):
    datetime = forms.DateTimeField(label='Date', widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id':'date', 'type':'date'}))
    clinic = forms.ModelChoiceField(label='Hospital', queryset=models.clinics.objects.all(), initial=0, widget=forms.Select(attrs={'class': 'form-control', 'id':'gate'}))
    Description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Please describe symptoms or situation' }))

class loginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'email', 'type':'email'}), required=True) 
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id':'password', 'type':'password'}), required=True)

class contactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Name' }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Email' }))
    subject = forms.CharField(label='subject', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Subject' }))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'id':'description', 'placeholder':'Messages' }))


