from django.urls import path
from . import views


urlpatterns = [    
    path('consultations', views.consultations.as_view(), name='Clinic_Consultation'),
    path('consultation/<int:consultation_id>/approve', views.Approveconsultations.as_view(), name='Approve_Consultation'),
    path('consultation/<int:consultation_id>/deny', views.Denyconsultations.as_view(), name='Deny_Consultation'),
    path('consultation/<int:consultation_id>/report', views.ConsultationReport.as_view(), name='Consultation_Report'),
    path('invoices', views.invoices.as_view(), name='Clinic_Bills'),
    path('profile', views.profile.as_view(), name='Clinic_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
]
