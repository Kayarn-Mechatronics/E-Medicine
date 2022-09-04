from django.urls import path
from . import views


urlpatterns = [    
    path('prescriptions', views.prescriptions.as_view(), name='Pharmacy_Presciptions'),
    path('bills', views.bills.as_view(), name='Pharmacy_Bills'),
    path('profile', views.profile.as_view(), name='Pharmacy_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
]
