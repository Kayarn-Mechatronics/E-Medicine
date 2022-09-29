from django.urls import path
from . import views


urlpatterns = [    
    path('prescriptions', views.prescriptions.as_view(), name='Pharmacy_Presciptions'),
    path('prescriptions/<int:consultation_id>/report', views.PrescriptionReport.as_view(), name='Prescription_Report'),
    path('invoices', views.bills.as_view(), name='Pharmacy_Bills'),
]
