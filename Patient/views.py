from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse, HttpRequest, HttpResponse 
from . import forms
# Create your views here.


#Let User Choose which view
class index(View):
    def get(self, request):
        return redirect(reverse('login'))

class login(View):
    template_name = 'Authentication/login.html'
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)

class consultations(View):
    template_name = 'Consultation/ConsultationPage.html'
    context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name, self.context)

    # def post(self, request):
    #     if request.POST.get('action') == 'add':
    #         form = forms.TarrifForm(request.POST)
    #         if form.is_valid():
    #             form.cleaned_data['customer_id'] = request.user.customer_id
    #             form.create()
    #             self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
    #             self.context['success'] = {'message': 'Tarrif updated successfully'}
    #             return render(request, self.template_name, self.context)
    #         else:
    #             self.context['tarrifForm'] = form
    #             self.context['errors'] = form.errors.get_json_data()
    #             return render(request, self.template_name, self.context)

    #     elif request.POST.get('action') == 'update':
    #         form = forms.TarrifForm(request.POST)
    #         if form.is_valid():
    #             form.update()
    #             self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
    #             self.context['success'] = {'message': 'Tarrif updated successfully'}
    #             return render(request, self.template_name, self.context)
    #         else:
    #             self.context['tarrifForm'] = form
    #             self.context['errors'] = form.errors.get_json_data()
    #             return render(request, self.template_name, self.context)

    #     elif request.POST.get('action') == 'delete':
    #         tarrif_id = request.POST.get('tarrif_id')
    #         models.Tarrif.objects.get(tarrif_id=tarrif_id).delete()
    #         self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
    #         return render(request, self.template_name, self.context)

    #     else:
    #         return HttpResponseBadRequest()


class pharmacy(View):
    template_name = 'Pharmacy/PharmacyPage.html'
    #context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


class bills(View):
    template_name = 'Bills/BillsPage.html'
    #context = {'ConsultationForm' : forms.ConsultationForm()}
    http_method_names = ['get', 'post']

    def get(self, request):
        #self.context['tarrifs'] = models.Tarrif.objects.filter(customer_id=request.user.customer_id.customer_id)
        #self.context['user'] = request.user
        return render(request, self.template_name)#, self.context)


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