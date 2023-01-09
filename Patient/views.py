from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from lib.pindo import send_sms
import datetime

import Clinics
from . import forms
from . import models


class index(View):
    def get(self, request):
        return redirect(reverse('login'))

class register(View):
    template_name = 'Authentication/register.html'
    http_method_names = ['get', 'post']
    context = {'RegisterForm' :  forms.registrationForm()}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form  = forms.registrationForm(request.POST)
        if form.is_valid():
            userobj = models.Users.objects.filter(email=form.cleaned_data['email'])
            if userobj.exists():
                #If user with email exists
                form.add_error(None, 'User with this email already exists, try another one or login.')
                self.context['SignUpForm'] = form
                self.context['errors'] = form.errors.get_json_data()['__all__']
                return render(request, self.template_name, context=self.context)
            else:
                #Validate Password
                if form.cleaned_data['password'] != form.cleaned_data['password_confirmation']:
                    form.add_error(None, 'Password and Password Confirmation must be the same')
                    self.context['SignUpForm'] = form
                    self.context['errors'] = form.errors.get_json_data()['__all__']
                    return render(request, self.template_name, context=self.context)
                else:
                    user_OBJ = models.Users(email=form.cleaned_data['email'], 
                                            first_name=form.cleaned_data['first_name'], 
                                            last_name=form.cleaned_data['last_name'], 
                                            phonenum=form.cleaned_data['phone'], 
                                            password=make_password(form.cleaned_data['password']),
                                            dob = form.cleaned_data['dob'],
                                            city=form.cleaned_data['city'],
                                            address=form.cleaned_data['address'],
                                            id_number=form.cleaned_data['id_number'],
                                            role='Patient', 
                                            is_relative=form.cleaned_data['is_relative'])
                    user_OBJ.save()
                    send_sms(user_OBJ.phonenum, 'Dear {0}, Thank you for registering as patient to E-Medicine. We look forward to working with you to improve the health of the people of Kirehe'.format(user_OBJ.first_name))
                    return redirect(reverse('login'))
        else:
            form.add_error(None, 'Please fill all fields and check the errors')
            self.context['SignUpForm'] = form
            self.context['errors'] = form.errors.get_json_data()['__all__']
            return render(request, self.template_name, context=self.context)

class clinic_register(View):
    template_name = 'Authentication/register-clinic.html'
    http_method_names = ['get', 'post']
    context = {'RegisterForm' :  forms.clinic_registrationForm()}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form  = forms.clinic_registrationForm(request.POST)
        if form.is_valid():
            userobj = models.Users.objects.filter(email=form.cleaned_data['email'])
            if userobj.exists():
                form.add_error(None, 'User with this email already exists, try another one or login.')
                self.context['SignUpForm'] = form
                self.context['errors'] = form.errors.get_json_data()['__all__']
                return render(request, self.template_name, context=self.context)
            else:
                if form.cleaned_data['password'] != form.cleaned_data['password_confirmation']:
                    form.add_error(None, 'Password and Password Confirmation must be the same')
                    self.context['SignUpForm'] = form
                    self.context['errors'] = form.errors.get_json_data()['__all__']
                    return render(request, self.template_name, context=self.context)
                else:
                    user_OBJ = models.Users(email=form.cleaned_data['email'], specialisation=form.cleaned_data['specialisation'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], phonenum=form.cleaned_data['phone'], password=make_password(form.cleaned_data['password']),
                        city=form.cleaned_data['city'],address=form.cleaned_data['address'],role='Clinic')
                    user_OBJ.save()
                    clinic_OBJ = models.clinics(name=form.cleaned_data['clinic'], doctor = user_OBJ )
                    clinic_OBJ.save()
                    send_sms(user_OBJ.phonenum, 'Dear {0}, Thank you for registering {1} as a new partner to E-Medicine. We look forward to working with you to improve the health of the citizens of Kirehe'.format(user_OBJ.first_name, clinic_OBJ.name))
                    return redirect(reverse('login'))
        else:
            form.add_error(None, 'Please fill all fields and check the errors')
            self.context['SignUpForm'] = form
            self.context['errors'] = form.errors.get_json_data()['__all__']
            return render(request, self.template_name, context=self.context)

class pharmacy_register(View):
    template_name = 'Authentication/register-pharmacy.html'
    http_method_names = ['get', 'post']
    context = {'RegisterForm' :  forms.pharmacy_registrationForm()}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form  = forms.pharmacy_registrationForm(request.POST)
        if form.is_valid():
            userobj = models.Users.objects.filter(email=form.cleaned_data['email'])
            if userobj.exists():
                form.add_error(None, 'User with this email already exists, try another one or login.')
                self.context['SignUpForm'] = form
                self.context['errors'] = form.errors.get_json_data()['__all__']
                return render(request, self.template_name, context=self.context)
            else:
                if form.cleaned_data['password'] != form.cleaned_data['password_confirmation']:
                    form.add_error(None, 'Password and Password Confirmation must be the same')
                    self.context['SignUpForm'] = form
                    self.context['errors'] = form.errors.get_json_data()['__all__']
                    return render(request, self.template_name, context=self.context)
                else:
                    user_OBJ = models.Users(email=form.cleaned_data['email'], specialisation='',first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], phonenum=form.cleaned_data['phone'], password=make_password(form.cleaned_data['password']),
                        city=form.cleaned_data['city'],address=form.cleaned_data['address'],role="Pharmacist")
                    user_OBJ.save()
                    pharmacy_OBJ = models.pharmacy(name=form.cleaned_data['pharmacy'], pharmacist = user_OBJ )
                    pharmacy_OBJ.save()
                    send_sms(user_OBJ.phonenum, 'Dear {0}, Thank you for registering {1} as a new partner to E-Medicine. We look forward to working with you to improve the health of the citizens of Kirehe.'.format(user_OBJ.first_name, pharmacy_OBJ.name))
                    return redirect(reverse('login'))
        else:
            form.add_error(None, 'Please fill all fields and check the errors')
            self.context['SignUpForm'] = form
            self.context['errors'] = form.errors.get_json_data()['__all__']
            return render(request, self.template_name, context=self.context)


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
                if user.role == "Patient":
                    auth.login(request, user)
                    return redirect(reverse('Patient_Consultation'))
                elif user.role == "Clinic":
                    auth.login(request, user)
                    return redirect(reverse('Clinic_Consultation'))
                elif user.role == "Pharmacist":
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
    context['today'] = '{0}-{1}-{2}'.format(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
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
                time = form.cleaned_data['time'],
                clinic = form.cleaned_data['clinic'],
                description = form.cleaned_data['Description']
            )
            consult.save()
            print(form.cleaned_data)
        self.context['consultations'] = models.Consultations.objects.filter(user_id=request.user.user_id)
        return render(request, self.template_name, self.context)


class CancelConsultations(View, LoginRequiredMixin):
    http_method_names = ['post']

    def post(self, request):
        obj = models.Consultations.objects.get(consultation_id=request.POST['consultation_id'])
        obj.delete()
        return redirect(reverse('Patient_Consultation'))
    
class pharmacy(View):
    template_name = 'Pharmacy/PharmacyPage.html'
    context = {'active' : 1}
    http_method_names = ['get', 'post']

    def get(self, request):
        self.context['prescriptions'] = models.Consultations.objects.filter(user_id=request.user.user_id, status='Served')
        self.context['user'] = request.user
        return render(request, self.template_name, self.context)


class bills(View):
    template_name = 'Bills/BillsPage.html'
    context = {'active' : 2}
    http_method_names = ['get', 'post']

    def get(self, request):
        self.context['bills'] = models.Consultations.objects.filter(user_id=request.user.user_id, status='Served')
        self.context['user'] = request.user
        return render(request, self.template_name, self.context)


class profile(View):
    template_name = 'Profile/ProfilePage.html'
    context = {'active' : 3}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name, self.context)


class contact(View):
    template_name = 'Contact/ContactPage.html'
    context = {'active' : 4}
    http_method_names = ['get', 'post']
    context['ContactForm'] = forms.contactForm()

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        return render(request, self.template_name, self.context)