from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from random import randint
import ELDERLY_CARE
from ELDERLY_CARE.models import Users,Consultant,Medical_shops
from smtplib import SMTPException, SMTPRecipientsRefused

# Create your views here.

def otp():
    otp = str(randint(100000,999999))
    return otp

def password_gen():
    pwd = "@"
    for i in range(2):
        ch=randint(65,90)
        pwd+=chr(ch)
    for i in range(2):
        ch=randint(97,122)
        pwd+=chr(ch)
    for i in range(3):
        num=randint(0,9)
        pwd+=str(num)
    return pwd


def send_otp(mail,otp):
    subject = "OTP"
    message = f"This is system generated mail please do not reply and share mail with anyone. This is your {otp}"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    try:
        send_mail(subject, message, sender, receivers)
        return True
    except(SMTPException, SMTPRecipientsRefused):
        return False
    
    
def send_registration_mail(mail):
    subject = "REGISTRATION SUCCESSFUL"
    message = "This is system generated mail please do not reply and share mail with anyone. Your registration is successful"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    send_mail(subject, message, sender, receivers)


def send_password(mail,pwd):
    subject = "FORGATE PASSWORD"
    message = f"This is system generated mail please do not reply and share mail with anyone. Your new passward is {pwd}"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    send_mail(subject, message, sender, receivers)


def send_password_change(mail):
    subject = "PASSWORD CHANGE SUCCESSFULLY"
    message = f"This is system generated mail please do not reply and share mail with anyone. Your passward has been changed successfully"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    send_mail(subject, message, sender, receivers)
    

def userRegistration(request):
    mail = request.POST.get("email")
    if len(Users.objects.filter(email = mail))>0:
        return JsonResponse("user with email id exist already",safe = False)
    
    ot = otp()
    output = send_otp(mail,ot)
    if output == False:
        return JsonResponse("invalid email id",safe = False)
    
    pwd = request.POST.get("password")
    cpwd = request.POST.get("confirmPassword")
    if pwd != cpwd:
        return JsonResponse("both passwords are different ",safe = False)
        
    usersRefVar = Users(user_name = request.POST.get("userName"),
                    birth_date = request.POST.get("birthDate"),
                    gender = request.POST.get("gender"),
                    mobile_self = request.POST.get("mobile1"),
                    mobile_family = request.POST.get("mobile2"),
                    email = mail,
                    home_no_name = request.POST.get("home"),
                    street_no_name = request.POST.get("street"),
                    area_name = request.POST.get("area"),
                    village_city = request.POST.get("villageCity"),
                    tehsil = request.POST.get("tehsil"),
                    district = request.POST.get("district"),
                    state = request.POST.get("state"),
                    country = request.POST.get("country"),
                    password = pwd,
                    otp = ot
                    )
    usersRefVar.save()
    return JsonResponse("Now please verify email and otp",safe = False)


def medicalShopRegistration(request):
    mail = request.POST.get("email")
    if len(Medical_shops.objects.filter(email = mail))>0:
        return JsonResponse("user with email id exist already",safe = False)
    
    ot = otp()
    output = send_otp(mail,ot)
    if output == False:
        return JsonResponse("invalid email id",safe = False)
    
    pwd = request.POST.get("password")
    cpwd = request.POST.get("confirmPassword")
    if pwd != cpwd:
        return JsonResponse("both passwords are different ",safe = False)
        
    medShRefVar = Medical_shops(shop_owner_name = request.POST.get("owner"),
                    pharmasist_regi_id = request.POST.get("pharmasistId"), 
                    mobile_no = request.POST.get("mobile"),
                    email = mail,
                    shop_name = request.POST.get("shopName"),
                    shop_regi_id = request.POST.get("shopId"),
                    shop_contact_no = request.POST.get("shopContact"),
                    street_no_name = request.POST.get("street"),
                    area_name = request.POST.get("area"),
                    village_city = request.POST.get("villageCity"),
                    tehsil = request.POST.get("tehsil"),
                    district = request.POST.get("district"),
                    state = request.POST.get("state"),
                    country = request.POST.get("country"),
                    password = pwd,
                    otp = ot
                    )
    medShRefVar.save()
    return JsonResponse("Now please verify email and otp",safe = False)


def ConsultantRegistration(request):
    mail = request.POST.get("email")
    if len(Consultant.objects.filter(email = mail))>0:
        return JsonResponse("user with email id exist already",safe = False)
    
    ot = otp()
    output = send_otp(mail,ot)
    if output == False:
        return JsonResponse("invalid email id",safe = False)
    
    pwd = request.POST.get("password")
    cpwd = request.POST.get("confirmPassword")
    if pwd != cpwd:
        return JsonResponse("both passwords are different ",safe = False)
        
    consultantRefVar = Users(consultant_name = request.POST.get("consultantName"),
                    gender = request.POST.get("gender"),
                    speciality_field = request.POST.get("speciality"),
                    consultant_regi_id = request.POST.get("consRegiId"),
                    mobile_no = request.POST.get("mobile"),
                    email = mail,
                    hospital_name = request.POST.get("hospName"),
                    hospital_regi_id = request.POST.get("hospId"),
                    hospital_contact_no = request.POST.get("hospContact"),
                    street_no_name = request.POST.get("street"),
                    area_name = request.POST.get("area"),
                    village_city = request.POST.get("villageCity"),
                    tehsil = request.POST.get("tehsil"),
                    district = request.POST.get("district"),
                    state = request.POST.get("state"),
                    country = request.POST.get("country"),
                    password = pwd,
                    otp = ot
                    )
    consultantRefVar.save()
    return JsonResponse("Now please verify email and otp",safe = False)


def verify_email(request):
    mail = request.POST.get("email")
    otp = request.POST.get("otp")
    try:
        data = Users.objects.get(email = mail)
        if data.otp == otp:
            data.email_verify = "verified"
            send_registration_mail(data.email)
            return JsonResponse("your profile created successfully")
        else:
            data.delete()
            return JsonResponse("invalid opt signup again")
    except ELDERLY_CARE.models.Users.DoesNotExist:
        try:
            data = Medical_shops.objects.get(email = mail)
            if data.otp == otp:
                data.email_verify = "verified"
                send_registration_mail(data.email)
                return JsonResponse("your profile created successfully")
            else:
                data.delete()
                return JsonResponse("invalid opt signup again")
        except ELDERLY_CARE.models.Medical_shops.DoesNotExist:
            try:
                data = Consultant.objects.get(email = mail)
                if data.otp == otp:
                    data.email_verify = "verified"
                    send_registration_mail(data.email)
                    return JsonResponse("your profile created successfully")
                else:
                    data.delete()
                    return JsonResponse("invalid opt signup again")
            except ELDERLY_CARE.models.Consultant.DoesNotExist:
                    return JsonResponse("invalid email id", safe = False)


def forgatePassword(request):
    mail = request.POST.get("email")
    try:
        data = Users.objects.get(email = mail)
        pwd = password_gen()
        data.password = pwd
        data.save()
        send_password(data.email,pwd)
        return JsonResponse("new password sent to your registered email id")
    except ELDERLY_CARE.models.Users.DoesNotExist:
        try:
            data = Medical_shops.objects.get(email = mail)
            pwd = password_gen()
            data.password = pwd
            data.save()
            send_password(data.email,pwd)
            return JsonResponse("new password sent to your registered email id")
        except ELDERLY_CARE.models.Medical_shops.DoesNotExist:
            try:
                data = Consultant.objects.get(email = mail)
                pwd = password_gen()
                data.password = pwd
                data.save()
                send_password(data.email,pwd)
                return JsonResponse("new password sent to your registered email id")
            except ELDERLY_CARE.models.Consultant.DoesNotExist:
                    return JsonResponse("invalid email id", safe = False)
            

def changePassword(request):
    mail = request.POST.get("email")
    oldPwd = request.POST.get("oldPwd")
    newPwd = request.POST.get("newPwd")
    try:
        data = Users.objects.get(email = mail, password = oldPwd)
        data.password = newPwd
        data.save()
        send_password_change(data.email)
        return JsonResponse("password change successfully")
    except ELDERLY_CARE.models.Users.DoesNotExist:
        try:
            data = Medical_shops.objects.get(email = mail, password = oldPwd)
            data.password = newPwd
            data.save()
            send_password_change(data.email)
            return JsonResponse("password change successfully")
        except ELDERLY_CARE.models.Medical_shops.DoesNotExist:
            try:
                data = Consultant.objects.get(email = mail, password = oldPwd)
                data.password = newPwd
                data.save()
                send_password_change(data.email)
                return JsonResponse("password change successfully")
            except ELDERLY_CARE.models.Consultant.DoesNotExist:
                    return JsonResponse("invalid email id or password", safe = False)