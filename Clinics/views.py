from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect 
from Patient import models
from Patient import forms as PatientForms
import Patient
from . import forms as ClinicForms
from lib.pindo import send_sms
from random import randint


class consultations(View, LoginRequiredMixin):
    template_name = 'ClinicConsultations/ConsultationPage.html'
    http_method_names = ['get', 'post']
    context = {}

    def get(self, request):
        clinic_id = models.clinics.objects.filter(doctor=request.user.user_id)
        self.context['consultations'] = models.Consultations.objects.filter(clinic = clinic_id[0])
        return render(request, self.template_name, self.context)


class ConsultationReport(View, LoginRequiredMixin):
    template_name = 'ClinicConsultations/ConsultationReportForm.html'
    http_method_names = ['get', 'post']
    context = {'ConsultationReportForm': ClinicForms.ConsultationReportForm()}

    def get(self, request, consultation_id):
        self.context['consultation'] = models.Consultations.objects.get(consultation_id=consultation_id)
        return render(request, self.template_name, self.context)

    def post(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        report = ClinicForms.ConsultationReportForm(request.POST)
        if report.is_valid():
            obj.clinic_report = report.cleaned_data['report']
            obj.status = 'Served'
            obj.pharmacy_id = report.cleaned_data['pharmacy']
            obj.prescription = report.cleaned_data['prescription']
            #obj.bill_clinic = report.cleaned_data['bill_pharmacy']
            obj.save()
        return redirect(reverse('Clinic_Consultation'))

class Approveconsultations(View, LoginRequiredMixin):
    http_method_names = ['get']
    context = {}

    def get(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        obj.status = 'Approved'
        obj.save()
        if obj.user_id.is_relative:
            coverage = '85%'
        else:
            coverage = '100%'
        pin = randint(100000,999999)
        send_sms(obj.user_id.phonenum, 'Dear {0}, We would like to notify you that your medical consultation appointment request at {1} on the {2} at {3} has been approved! Please note that Cimerwa PLC will cover {4} of the cost. Please use the following Pin {5} to request service'.format(obj.user_id.first_name, obj.clinic.name, obj.date.date(), obj.time, coverage, pin))           
        
        return HttpResponseRedirect(reverse('Clinic_Consultation'))

class Denyconsultations(View, LoginRequiredMixin):
    http_method_names = ['get']
    context = {}

    def get(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        obj.status = 'Denied'
        obj.save()
        send_sms(obj.user_id.phonenum, 'Dear {0}, We would like to notify you that your medical consultation appointment request at {1} on the {2} at {3} has been denied! Please login back to insurance-mgt.herokuapp.com to book another appointment!.'.format(obj.user_id.first_name, obj.clinic.name, obj.date.date(), obj.time))           
        return HttpResponseRedirect(reverse('Clinic_Consultation'))

class invoices(View, LoginRequiredMixin):
    template_name = 'Invoices/InvoicesPage.html'
    http_method_names = ['get', 'post']
    context = {'active': 1}

    def get(self, request):
        clinic_id = models.clinics.objects.filter(doctor=request.user.user_id)
        self.context['invoices'] = models.Consultations.objects.filter(clinic = clinic_id[0])
        return render(request, self.template_name, self.context)


class profile(View, LoginRequiredMixin):
    template_name = 'Profile/ProfilePage.html'
    #context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


class contact(View, LoginRequiredMixin):
    template_name = 'Contact/ContactPage.html'
    http_method_names = ['get', 'post']
    context = {}

    def get(self, request):
        self.context['ContactForm'] = PatientForms.contactForm()
        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context['ContactForm'] = PatientForms.contactForm()
        return render(request, self.template_name, self.context)