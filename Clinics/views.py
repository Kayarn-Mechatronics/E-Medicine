from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect 
from Patient import models
from . import forms as ClinicForms


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

        return render(request, self.template_name, self.context)

class Approveconsultations(View, LoginRequiredMixin):
    http_method_names = ['post']
    context = {}

    def post(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        obj.status = 'Approved'
        obj.save()
        return HttpResponseRedirect(reverse('Clinic_Consultation'))

class Denyconsultations(View, LoginRequiredMixin):
    http_method_names = ['post']
    context = {}

    def post(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        obj.status = 'Deny'
        obj.save()
        return HttpResponseRedirect(reverse('Clinic_Consultation'))

class invoices(View, LoginRequiredMixin):
    template_name = 'Bills/BillsPage.html'
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