from django.urls import path
from . import views


urlpatterns = [    
    path('consultation', views.consultations.as_view(), name='Patient_Consultation'),
    path('pharmacy', views.pharmacy.as_view(), name='Patient_Presciptions'),
]
