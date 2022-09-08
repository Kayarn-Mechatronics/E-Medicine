# Generated by Django 4.1 on 2022-09-08 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0010_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('patient', 'patient'), ('clinic', 'clinic'), ('pharmacist', 'pharmacist')], default='patient', max_length=255),
        ),
    ]
