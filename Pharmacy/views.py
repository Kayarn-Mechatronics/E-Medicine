from operator import indexOf
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse, HttpRequest, HttpResponse 

from Patient import models
from . import forms
# Create your views here.



class prescriptions(LoginRequiredMixin, View):
    template_name = 'Pharmacist/PharmacistPage.html'
    context = {}
    http_method_names = ['get', 'post']

    def get(self, request):
        self.context['prescriptions'] = models.Consultations.objects.filter(pharmacy_id=models.pharmacy.objects.get(pharmacist = request.user.user_id))
        print(self.context)
        self.context['user'] = request.user
        return render(request, self.template_name, self.context)


class PrescriptionReport(View, LoginRequiredMixin):
    template_name = 'Pharmacist/PrescriptionReport.html'
    http_method_names = ['get', 'post']
    context = {'ConsultationReportForm': forms.PrescriptionReportForm()}

    def get(self, request, consultation_id):
        self.context['consultation'] = models.Consultations.objects.get(consultation_id=consultation_id)
        return render(request, self.template_name, self.context)

    def post(self, request, consultation_id):
        obj = models.Consultations.objects.get(consultation_id=consultation_id)
        report = forms.PrescriptionReportForm(request.POST)
        if report.is_valid():
            obj.pin_pharmacy = True
            obj.bill_pharmacy = report.cleaned_data['bill']
            obj.save()
        return redirect(reverse('Pharmacy_Presciptions'))


class bills(LoginRequiredMixin, View):
    template_name = 'Pharmacist/PrescriptionsBills.html'
    http_method_names = ['get', 'post']
    context = {}

    def get(self, request):
        self.context['user'] = request.user
        self.context['bills'] = models.Consultations.objects.filter(pharmacy_id=models.pharmacy.objects.get(pharmacist = request.user.user_id))
        return render(request, self.template_name, self.context)