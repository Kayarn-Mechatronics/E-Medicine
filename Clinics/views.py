from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse, HttpRequest, HttpResponse 
from Patient import models


class consultations(View):
    template_name = 'ClinicConsultations/ConsultationPage.html'
    http_method_names = ['get', 'post']
    context = {}

    def get(self, request):
        clinic_id = models.clinics.objects.get(doctor=request.user.user_id)
        self.context['consultations'] = models.Consultations.objects.filter(clinic = clinic_id)
        return render(request, self.template_name)


class invoices(View):
    template_name = 'Bills/BillsPage.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        return render(request, self.template_name)


class profile(View):
    template_name = 'Profile/ProfilePage.html'
    #context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


class contact(View):
    template_name = 'Contact/ContactPage.html'
    #context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)