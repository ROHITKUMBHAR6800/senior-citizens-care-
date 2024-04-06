from django.db import models
from django.utils import timezone
# from datetime import datetime

# Create your models here.

class Users(models.Model):

    email = models.EmailField(primary_key = True)
    user_name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    gender = models.CharField(max_length = 10)
    mobile_self = models.CharField(max_length = 13)
    mobile_family = models.CharField(max_length = 13)
    home_no_name = models.CharField(max_length = 100)
    street_no_name = models.CharField(max_length = 100)
    area_name = models.CharField(max_length = 100)
    village_city = models.CharField(max_length = 100) 
    tehsil = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100) 
    country = models.CharField(max_length = 100)
    join_date = models.DateTimeField(default = timezone.now)
    password = models.CharField(max_length = 50)
    otp = models.CharField(max_length = 6)
    email_verify = models.CharField(max_length = 10, default = "unverified")
    

class Consultant(models.Model):

    consultant_regi_id = models.CharField(max_length = 100,primary_key = True)
    consultant_name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    speciality_field = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 13)
    email = models.EmailField(unique = True)
    hospital_name = models.CharField(max_length = 100)
    hospital_regi_id = models.CharField(max_length = 100)
    hospital_contact_no = models.CharField(max_length = 13)
    street_no_name = models.CharField(max_length = 100)
    area_name = models.CharField(max_length = 100)
    village_city = models.CharField(max_length = 100) 
    tehsil = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100) 
    country = models.CharField(max_length = 100)
    join_date = models.DateTimeField(default = timezone.now)
    password = models.CharField(max_length = 50)
    otp = models.CharField(max_length = 6)
    email_verify = models.CharField(max_length = 10, default = "unverified")


class Medical_shops(models.Model):

    shop_regi_id = models.CharField(max_length = 100,primary_key = True)
    shop_owner_name = models.CharField(max_length = 100)
    pharmasist_regi_id=models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 13)
    email = models.EmailField(unique = True)
    shop_name = models.CharField(max_length = 100)
    shop_contact_no = models.CharField(max_length = 13)
    street_no_name = models.CharField(max_length = 100)
    area_name = models.CharField(max_length = 100)
    village_city = models.CharField(max_length = 100) 
    tehsil = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100) 
    country = models.CharField(max_length = 100)
    join_date = models.DateTimeField(default = timezone.now)
    password = models.CharField(max_length = 50)
    otp = models.CharField(max_length = 6)
    email_verify = models.CharField(max_length = 10, default = "unverified")


class medicine_orders(models.Model):

    oder_id = models.BigAutoField(primary_key = True)
    order_item = models.CharField(max_length = 100)
    item_quantity = models.IntegerField()
    price = models.IntegerField()
    order_status = models.CharField(max_length = 20, default="pending")
    order_date = models.DateTimeField(default=timezone.now)
    delivery_time = models.DateTimeField(default=timezone.now)
    shop_id = models.CharField(max_length = 100)
    shop_name = models.CharField(max_length=100)
    shop_contact = models.CharField(max_length = 13)
    shop_owner = models.CharField(max_length = 100)
    owner_mobile = models.CharField(max_length = 13)
    shop_address = models.CharField(max_length = 300)
    user_name = models.CharField(max_length = 100)
    user_email = models.EmailField()
    user_mobile_self = models.CharField(max_length = 13)
    user_mobile_family = models.CharField(max_length = 13)
    user_address = models.CharField(max_length = 300)
    

class appointment(models.Model):

    user_name = models.CharField(max_length = 100)
    user_email = models.EmailField()
    user_mobile = models.CharField(max_length = 13)
    user_address = models.CharField(max_length = 300)
    illness_type = models.CharField(max_length = 100)
    entry_date = models.DateTimeField(default = timezone.now)
    ask_appointment_date = models.DateField()
    appointment_status = models.CharField(max_length = 20, default="pending")
    appointment_time = models.DateTimeField(default=timezone.now)
    consultant_id = models.CharField(max_length = 100)
    specility_type = models.CharField(max_length = 100)
    hospital_id = models.CharField(max_length = 100)
    hospital_name = models.CharField(max_length=100)
    hospital_contact = models.CharField(max_length = 13)
    hospital_address = models.CharField(max_length = 300)

