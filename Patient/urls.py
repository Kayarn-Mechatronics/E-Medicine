from django.urls import path
from . import views


urlpatterns = [   
    path('', views.index.as_view(), name='index'), 
	path('login', views.login.as_view(), name='login'),
    path('consultation', views.consultations.as_view(), name='Patient_Consultation'),
    path('pharmacy', views.pharmacy.as_view(), name='Patient_Presciptions'),
    path('bills', views.bills.as_view(), name='Patient_Bills'),
    path('profile', views.profile.as_view(), name='Patient_Profile'),
    path('contact-us', views.contact.as_view(), name='Contact-us'),
    path('logout', views.logout.as_view(), name='logout'),
]
