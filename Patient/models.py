from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, User


class Users(AbstractUser):
    Roles = [
		('Patient', 'patient'),
		('Clinic', 'clinic'),
		('Pharmacist', 'pharmacist')]

    user_id = models.SmallAutoField(primary_key=True, unique=True, editable=False)
    email = models.EmailField(db_column='Email', unique=True)
    phonenum = models.CharField(db_column='PhoneNum', max_length=30, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Roles, default='patient')
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_relative = models.BooleanField(blank=True, null=True)
    id_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'Users'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class clinics(models.Model):
    clinic_id = models.SmallAutoField(db_column='clinic_id', primary_key=True, editable=False)
    name = models.CharField(db_column='Name', max_length=50)
    doctor = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'Clinic'
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.name



class Consultations(models.Model):
    consultation_id = models.SmallAutoField(db_column='Consultation_ID', primary_key=True, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    date =  models.DateTimeField(db_column='Datetime', blank=True, null=True)
    clinic = models.ForeignKey(clinics, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=40, null=True, blank=True, default='Pending')


    class Meta:
        db_table = 'Consultations'
        verbose_name_plural = "Consultations"

    def __str__(self):
        return self.user_id.email


class ConsultationsReport(models.Model):
    report_id = models.SmallAutoField(db_column='report_id', primary_key=True, editable=False)
    consultation_id = models.ForeignKey(Consultations, on_delete=models.CASCADE, blank=True)
    comment = models.TextField(db_column='comment', blank=True, max_length=100)
    prescription = models.TextField(db_column='prescription', blank=True, max_length=100)

    class Meta:
        db_table = 'ConsultationsReport'
        verbose_name_plural = "ConsultationsReports"

    def __str__(self):
        return str(self.report_id)


class Contact(models.Model):
    message_id = models.SmallAutoField(db_column='report_id', primary_key=True, editable=False)
    name = models.CharField(db_column="Names", max_length=100, editable=False)
    email = models.EmailField(db_column="email", blank=True, null=True)
    subject = models.CharField(db_column="subject", blank=True, null=True, max_length=500)
    message = models.TextField(db_column="message", blank=True, null=True, max_length=1000)

    class Meta:
        db_table = 'Contacts'
        verbose_name_plural = "Contacts"

    def __str__(self):
        return str(self.email)