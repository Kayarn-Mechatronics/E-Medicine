from django.urls import path
from . import views


urlpatterns = [    
    path('consultations', views.consultations.as_view(), name='Clinic_Consultation'),
    path('bills', views.invoices.as_view(), name='Clinic_Bills'),
    path('profile', views.profile.as_view(), name='Clinic_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
]
