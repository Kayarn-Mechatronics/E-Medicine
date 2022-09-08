from webbrowser import get
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse, HttpRequest, HttpResponse 
from django.contrib import auth

import Clinics
from . import forms
from . import models
# Create your views here.


#Let User Choose which view
class index(View):
    def get(self, request):
        return redirect(reverse('login'))

class register(View):
    template_name = 'Authentication/register.html'
    http_method_names = ['get', 'post']
    context = {'RegisterForm' :  forms.registrationForm()}

    def get(self, request):
        return render(request, self.template_name, self.context)

class login(View):
    template_name = 'Authentication/login.html'
    http_method_names = ['get', 'post']
    context = {'loginForm' :  forms.loginForm()}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if int(user.role) == 0:
                    auth.login(request, user)
                    return redirect(reverse('Patient_Consultation'))
                elif int(user.role) == 1:
                    auth.login(request, user)
                    return redirect(reverse('Clinic_Consultation'))
                elif int(user.role) == 2:
                    auth.login(request, user)
                    return redirect(reverse('Pharmacy_Presciptions'))
                else:
                    form.add_error(None, "User does not have a role!")
                    self.context['LoginForm'] = form
                    self.context['errors'] = form.errors.get_json_data()['__all__']
                    return render(request, self.template_name, context=self.context)

            else:
                form.add_error(None, "Incorect email or password!")
                self.context['LoginForm'] = form
                self.context['errors'] = form.errors.get_json_data()['__all__']
                return render(request, self.template_name, context=self.context)
        else:
            form.add_error(None, "Please fill all the fields & check for errors")
            self.context['LoginForm'] = form
            self.context['errors'] = form.errors.get_json_data()['__all__']
            return render(request, self.template_name, context=self.context)
        
class logout(View, LoginRequiredMixin):
    template_name = 'Authentication/login.html'
    http_method_names = ['get', 'post']
    context = {'loginForm' :  forms.loginForm()}

    def get(self, request):
        user = request.user
        auth.logout(request)
        return render(request, self.template_name, self.context)

class consultations(View, LoginRequiredMixin):
    template_name = 'Consultation/ConsultationPage.html'
    context = {'ConsultationForm' : forms.ConsultationForm()}
    context['active'] = 0
    http_method_names = ['get', 'post']

    def get(self, request):
        self.context['consultations'] = models.Consultations.objects.filter(user_id=request.user.user_id)
        self.context['user'] = request.user
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = forms.ConsultationForm(request.POST)
        if form.is_valid():
            consult = models.Consultations.objects.create(
                user_id = request.user,
                date = form.cleaned_data['datetime'],
                clinic = form.cleaned_data['clinic'],
                description = form.cleaned_data['Description']
            )
            consult.save()
            print(form.cleaned_data)
        self.context['consultations'] = models.Consultations.objects.filter(user_id=request.user.user_id)
        return render(request, self.template_name, self.context)

    


class pharmacy(View):
    template_name = 'Pharmacy/PharmacyPage.html'
    context = {'active' : 1}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


class bills(View):
    template_name = 'Bills/BillsPage.html'
    context = {'active' : 2}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


class profile(View):
    template_name = 'Profile/ProfilePage.html'
    context = {'active' : 3}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


class contact(View):
    template_name = 'Contact/ContactPage.html'
    context = {'active' : 4}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)