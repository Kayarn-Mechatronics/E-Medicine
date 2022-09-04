from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, User


class Users(AbstractUser):
    user_id = models.SmallAutoField(primary_key=True, unique=True, editable=False)
    email = models.EmailField(db_column='Email', unique=True)
    phonenum = models.CharField(db_column='PhoneNum', max_length=30, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    username = None
    mail_verified = models.CharField(max_length=50)

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



    class Meta:
        db_table = 'Clinic'
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.clinic_id



class Consultations(models.Model):
    consultation_id = models.SmallAutoField(db_column='Consultation_ID', primary_key=True, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    date =  models.DateTimeField(db_column='Datetime', blank=True, null=True)
    clinic_id = None


    class Meta:
        db_table = 'Consultations'
        verbose_name_plural = "Consultations"

    def __str__(self):
        return self.consultation_id