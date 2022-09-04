from django.urls import path
from . import views


urlpatterns = [    
    path('consultation', views.consultations.as_view(), name='Patient_Consultation'),
    path('bills', views.invoices.as_view(), name='Patient_Bills'),
    path('profile', views.profile.as_view(), name='Patient_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
]
