from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse, HttpRequest, HttpResponse 
from django.contrib import auth
from . import forms
# Create your views here.


#Let User Choose which view
class index(View):
    def get(self, request):
        return redirect(reverse('login'))

class login(View):
    template_name = 'Authentication/login.html'
    http_method_names = ['get', 'post']
    context = {'loginForm' :  forms.loginForm()}

    def get(self, request):
        self.context['user'] = request.user
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = forms.loginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)

                return redirect(reverse('Patient_Consultation'))
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
        


class consultations(View):
    template_name = 'Consultation/ConsultationPage.html'
    context = {'ConsultationForm' : forms.ConsultationForm()}
    context['active'] = 0
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        self.context['user'] = request.user
        print(self.context)
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