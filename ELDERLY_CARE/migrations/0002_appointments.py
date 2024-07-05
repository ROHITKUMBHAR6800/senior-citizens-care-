# Generated by Django 5.0.4 on 2024-04-08 14:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ELDERLY_CARE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='appointments',
            fields=[
                ('appointment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_gender', models.CharField(max_length=10)),
                ('user_birth_date', models.DateField()),
                ('user_email', models.EmailField(max_length=254)),
                ('user_mobile', models.CharField(max_length=13)),
                ('user_address', models.CharField(max_length=300)),
                ('illness_type', models.CharField(max_length=100)),
                ('entry_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ask_appointment_date', models.DateField()),
                ('appointment_status', models.CharField(default='pending', max_length=20)),
                ('given_appointment_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('consultant_id', models.CharField(max_length=100)),
                ('consultant_name', models.CharField(max_length=100)),
                ('consultant_gender', models.CharField(max_length=10)),
                ('speciality_type', models.CharField(max_length=100)),
                ('hospital_id', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_contact', models.CharField(max_length=13)),
                ('hospital_address', models.CharField(max_length=300)),
            ],
        ),
    ]