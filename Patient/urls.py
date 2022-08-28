from django.urls import path
from . import views


urlpatterns = [    
    path('consultation', views.consultations.as_view(), name='Patient_Consultation'),
]
