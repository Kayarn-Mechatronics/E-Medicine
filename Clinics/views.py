from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect 
from Patient import models
from . import forms as ClinicForms
from lib.pindo import send_sms


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
            obj.prescriptions = report.cleaned_data['prescription']
            obj.bill_clinic = report.cleaned_data['bill']
            obj.paid_clinic = report.cleaned_data['paid']
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
        send_sms(obj.user_id.phonenum, 'Dear {0}, We would to notify you that your medical consultation appointment request at {1} on the {2} has been approved! Please note that Cimerwa PLC will cover {3} of the cost.'.format(obj.user_id.first_name, obj.clinic.name, obj.date, coverage))           
        
        return HttpResponseRedirect(reverse('Clinic_Consultation'))

class Denyconsultations(View, LoginRequiredMixin):
    http_method_names = ['get']
    context = {}

    def get(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        obj.status = 'Denied'
        obj.save()
        send_sms(obj.user_id.phonenum, 'Dear {0}, We would to notify you that your medical consultation appointment request at {1} on the {2} has been denied! Please login back to insurance-mgt.herokuapp.com to book another appointment!.'.format(obj.user_id.first_name, obj.clinic.name, obj.date))           
        return HttpResponseRedirect(reverse('Clinic_Consultation'))

class invoices(View, LoginRequiredMixin):
    template_name = 'Invoices/InvoicesPage.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        return render(request, self.template_name)


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
    #context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)