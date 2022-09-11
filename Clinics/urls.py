from django.urls import path
from . import views


urlpatterns = [    
    path('consultations', views.consultations.as_view(), name='Clinic_Consultation'),
    path('consultations/<str:consultation_id>/approve', views.Approveconsultations.as_view(), name='approve_Consultation'),
    path('consultations/<str:consultation_id>/deny', views.Denyconsultations.as_view(), name='deny_Consultation'),
    #path('consultations/<str:consultations_id>', views.view_consultation.as_view(), name='View_Consultations'),
    path('bills', views.invoices.as_view(), name='Clinic_Bills'),
    path('profile', views.profile.as_view(), name='Clinic_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
]
