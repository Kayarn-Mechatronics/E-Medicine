from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, User
from datetime import date


class Users(AbstractUser):
    Roles = [
		('Patient', 'Patient'),
		('Clinic', 'Clinic'),
		('Pharmacist', 'Pharmacist')]

    user_id = models.SmallAutoField(primary_key=True, unique=True, editable=False)
    email = models.EmailField(db_column='Email', unique=True)
    phonenum = models.CharField(db_column='PhoneNum', max_length=30, blank=True, null=True)
    role = models.CharField(max_length=255, choices=Roles, default='Patient')
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    is_relative = models.BooleanField(blank=True, null=True)
    id_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    specialisation = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'Users'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name + ' '  +self.last_name

    @property
    def age(self):
        try:
            today = date.today()
            return str(today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))) + "Years Old"
        except AttributeError:
            return ''



class clinics(models.Model):
    clinic_id = models.SmallAutoField(db_column='clinic_id', primary_key=True, editable=False)
    name = models.CharField(db_column='Name', max_length=50)
    doctor = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'Clinic'
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.name + ' - Dr.' + self.doctor.first_name + ' ' + self.doctor.last_name + ' - ' + self.doctor.specialisation


class pharmacy(models.Model):
    pharmacy_id = models.SmallAutoField(db_column='pharmacy_id', primary_key=True, editable=False)
    name = models.CharField(db_column='Name', max_length=50)
    pharmacist = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'Pharmacy'
        verbose_name_plural = "Pharmacies"

    def __str__(self):
        return self.name


class Consultations(models.Model):
    States = [
        ('Served', 'Served'),
		('Approved', 'Approved'),
		('Pending', 'Pending'),
		('Denied', 'Pending')]
    consultation_id = models.SmallAutoField(db_column='Consultation_ID', primary_key=True, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    date =  models.DateTimeField(db_column='Datetime', blank=True, null=True)
    time =  models.TimeField(db_column='time', blank=True, null=True)
    clinic = models.ForeignKey(clinics, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=255, choices=States, default='Pending')
    clinic_report = models.TextField(max_length=1000, null=True, blank=True)
    clinic_report_date = models.DateTimeField(db_column='report_date', blank=True, null=True)
    pharmacy_id = models.ForeignKey(pharmacy, on_delete=models.CASCADE, blank=True, null=True)
    prescription = models.CharField(max_length=500, null=True, blank=True)
    bill_pharmacy = models.BigIntegerField(null=True, blank=True)
    pin_pharmacy = models.BooleanField(null=True, blank=True, default=False)
    

    class Meta:
        db_table = 'Consultations'
        verbose_name_plural = "Consultations"

    def __str__(self):
        return self.user_id.email
    
    @property
    def pharmacy_balance(self):
        if self.user_id.is_relative:
            return self.bill_pharmacy * 0.85
        else:
            return 0

    @property
    def patient_balance(self):
        if self.user_id.is_relative:
            return self.bill_pharmacy * 0.15
        else:
            return 0


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