from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from random import randint
import ELDERLY_CARE
from ELDERLY_CARE.models import Users,Consultant,Medical_shops,medicine_orders,appointments
from smtplib import SMTPException, SMTPRecipientsRefused
from django.db.models import Q

# Create your views here.

# 6 digit otp will be created by using folling the function
def otp():
    otp = str(randint(100000,999999))
    return otp


# 8 digit password will be created by using folling the function
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


# otp will be send by using folling the function and if there any invalid email address then expect block will run
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
    
    
# this function will be used to send mail-registration successful
def send_registration_mail(mail):
    subject = "REGISTRATION SUCCESSFUL"
    message = "This is system generated mail please do not reply and share mail with anyone. Your registration is successful"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    send_mail(subject, message, sender, receivers)


# this function will be used to send mail-forgate password
def send_password(mail,pwd):
    subject = "FORGATE PASSWORD"
    message = f"This is system generated mail please do not reply and share mail with anyone. Your new passward is {pwd}"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    send_mail(subject, message, sender, receivers)


# this function will be used to send mail-password change successfully
def send_password_change(mail):
    subject = "PASSWORD CHANGE SUCCESSFULLY"
    message = f"This is system generated mail please do not reply and share mail with anyone. Your passward has been changed successfully"
    sender = "phchol06082001@gmail.com"
    receivers = [mail]
    send_mail(subject, message, sender, receivers)
    

# this function will be used to sign up new users
def userRegistration(request):
    if request.method == 'POST':
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
    else:
        return JsonResponse(" invalid method",safe = False)


# this function will be used to sign up new medical shops
def medicalShopRegistration(request):
    if request.method == 'POST':
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
    else:
        return JsonResponse(" invalid method",safe = False)


# this function will be used to sign up new consultant
def ConsultantRegistration(request):
    if request.method == 'POST':
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
            
        consultantRefVar = Consultant(consultant_name = request.POST.get("consultantName"),
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
    else:
        return JsonResponse(" invalid method",safe = False)


# this function will be used to verify email id
def verify_email(request):
    if request.method == 'POST':
        mail = request.POST.get("email")
        otp = request.POST.get("otp")
        try:
            data = Users.objects.get(email = mail)
            if data.otp == otp:
                data.email_verify = "verified"
                send_registration_mail(data.email)
                return JsonResponse("your profile created successfully",safe = False)
            else:
                data.delete()
                return JsonResponse("invalid opt signup again",safe = False)
        except ELDERLY_CARE.models.Users.DoesNotExist:
            try:
                data = Medical_shops.objects.get(email = mail)
                if data.otp == otp:
                    data.email_verify = "verified"
                    send_registration_mail(data.email)
                    return JsonResponse("your profile created successfully",safe = False)
                else:
                    data.delete()
                    return JsonResponse("invalid opt signup again",safe = False)
            except ELDERLY_CARE.models.Medical_shops.DoesNotExist:
                try:
                    data = Consultant.objects.get(email = mail)
                    if data.otp == otp:
                        data.email_verify = "verified"
                        send_registration_mail(data.email)
                        return JsonResponse("your profile created successfully",safe = False)
                    else:
                        data.delete()
                        return JsonResponse("invalid opt signup again")
                except ELDERLY_CARE.models.Consultant.DoesNotExist:
                        return JsonResponse("invalid email id", safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)


# this function will be used to genate new password and insert it in perticular record
def forgatePassword(request):
    if request.method == 'POST':
        mail = request.POST.get("email")
        try:
            data = Users.objects.get(email = mail)
            pwd = password_gen()
            data.password = pwd
            data.save()
            send_password(data.email,pwd)
            return JsonResponse("new password sent to your registered email id",safe = False)
        except ELDERLY_CARE.models.Users.DoesNotExist:
            try:
                data = Medical_shops.objects.get(email = mail)
                pwd = password_gen()
                data.password = pwd
                data.save()
                send_password(data.email,pwd)
                return JsonResponse("new password sent to your registered email id",safe = False)
            except ELDERLY_CARE.models.Medical_shops.DoesNotExist:
                try:
                    data = Consultant.objects.get(email = mail)
                    pwd = password_gen()
                    data.password = pwd
                    data.save()
                    send_password(data.email,pwd)
                    return JsonResponse("new password sent to your registered email id",safe = False)
                except ELDERLY_CARE.models.Consultant.DoesNotExist:
                        return JsonResponse("invalid email id", safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
            

# this function will be used to change old password by new password
def changePassword(request):
    if request.method == 'POST':
        mail = request.POST.get("email")
        oldPwd = request.POST.get("oldPwd")
        newPwd = request.POST.get("newPwd")
        try:
            data = Users.objects.get(email = mail, password = oldPwd)
            data.password = newPwd
            data.save()
            send_password_change(data.email)
            return JsonResponse("password change successfully",safe = False)
        except ELDERLY_CARE.models.Users.DoesNotExist:
            try:
                data = Medical_shops.objects.get(email = mail, password = oldPwd)
                data.password = newPwd
                data.save()
                send_password_change(data.email)
                return JsonResponse("password change successfully",safe = False)
            except ELDERLY_CARE.models.Medical_shops.DoesNotExist:
                try:
                    data = Consultant.objects.get(email = mail, password = oldPwd)
                    data.password = newPwd
                    data.save()
                    send_password_change(data.email)
                    return JsonResponse("password change successfully",safe = False)
                except ELDERLY_CARE.models.Consultant.DoesNotExist:
                        return JsonResponse("invalid email id or password", safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
            

# this fuction will fecth all related location medical shops
def searchMedicalShop(request):
    if request.method == 'POST':
        loc = request.POST.get("location")
        data = Medical_shops.objects.filter( 
                    Q(street_no_name = loc) |
                    Q(area_name = loc) |
                    Q(village_city = loc) | 
                    Q(tehsil = loc) |
                    Q(district = loc) |
                    Q(state = loc) |
                    Q(country = loc) 
                )
        num=1
        shop_list={}
        for records in data:
            shop_list[num]=f"{records.shop_name}, {records.shop_contact_no}, {records.street_no_name}, {records.area_name}, {records.village_city}, {records.tehsil}, {records.district}, {records.state}, {records.country},{records.shop_owner_name}, {records.mobile_no}"
            num+=1
        if len(shop_list)>0:
            return JsonResponse(shop_list)
        else:
            return JsonResponse("no result found please provide another location",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

def medicinesOrder(request):
    if request.method == 'POST':
        shopId = request.POST.get("shopId")
        userMail = request.POST.get("userEmail")
        orderItem = request.POST.get("medicine")
        itemQuantity = request.POST.get("qaunt")
        try:
            shop_data = Medical_shops.objects.get(shop_regi_id = shopId)
            user_data = Users.objects.get(email = userMail)
            medOrderRefVar = medicine_orders(
                        order_item = orderItem,
                        item_quantity = itemQuantity,
                        shop_id = shop_data.shop_regi_id,
                        shop_name = shop_data.shop_name,
                        shop_contact = shop_data.shop_contact_no,
                        shop_owner = shop_data.shop_owner_name,
                        owner_mobile = shop_data.mobile_no,
                        shop_address = f"{shop_data.street_no_name}, {shop_data.area_name}, {shop_data.village_city}, {shop_data.tehsil}, {shop_data.district}, {shop_data.state}, {shop_data.country}.",
                        user_name = user_data.user_name,
                        user_email = userMail,
                        user_mobile_self = user_data.mobile_self,
                        user_mobile_family = user_data.mobile_family,
                        user_address = f"{user_data.home_no_name}, {user_data.street_no_name}, {user_data.area_name}, {user_data.village_city}, {user_data.tehsil}, {user_data.district}, {user_data.state}, {user_data.country}."
                    )
            medOrderRefVar.save()
            return JsonResponse("order successful",safe = False)
        except:
            return JsonResponse("invalid credintials",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# This function would provide all orders of the shop
def shopAllOrder(request):
    if request.method == 'POST':
        shopId = request.POST.get("shopId") #shopId = shop_regi_id
        try:
            data = medicine_orders.objects.get(shop_id = shopId)
            output = []
            for order in data:
                order_data = {
                    "orderId": order.order_id,
                    "medicine": order.order_item,
                    "quant.": order.item_quantity,
                    "price": order.price,
                    "placedTime": order.order_date,
                    "status": order.order_status,
                    "deliveryTime": order.delivery_time,
                    "name": order.user_name,
                    "email": order.user_email,
                    "mobile_self": order.user_mobile_self,
                    "mobile_family": order.user_mobile_family,
                    "address": order.user_address
                }
                output.append(order_data)
            return JsonResponse(output, safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid credintial",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# This function would provide all orders of the user
def userAllOrder(request):
    if request.method == 'POST':
        mail = request.POST.get("shopId") #shopId = shop_regi_id
        try:
            data = medicine_orders.objects.get(user_email = mail)
            output = []
            for order in data:
                order_data = {
                    "orderId": order.order_id,
                    "medicine": order.order_item,
                    "quant.": order.item_quantity,
                    "price": order.price,
                    "placedTime": order.order_date,
                    "status": order.order_status,
                    "deliveryTime": order.delivery_time,
                    "name": order.shop_name,
                    "shop contact": order.shop_contact,
                    "owner": order.shop_owner,
                    "mobile": order.owner_mobile,
                    "address": order.shop_address
                }
                output.append(order_data)
            return JsonResponse(output, safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid credintial",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)


# This function would provide order details to shops
def shopOrderView(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            output = {}
            output["orderId"] = orderId
            output["medicine"] = data.order_item
            output["quant."] = data.item_quantity
            output["price"] = data.price
            output["placedTime"] = data.order_date
            output["status"] = data.order_status
            output["deliveryTime"] = data.delivery_time
            output["name"] = data.shop_name
            output["shop contact"] = data.shop_contact
            output["onwer"] = data.shop_owner
            output["mobile"] = data.owner_mobile
            output["address"] = data.shop_address
            return JsonResponse(output)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# This function would provide order details to users
def userOrderView(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            output = {}
            output["orderId"] = orderId
            output["medicine"] = data.order_item
            output["quant."] = data.item_quantity
            output["price"] = data.price
            output["placedTime"] = data.order_date
            output["status"] = data.order_status
            output["deliveryTime"] = data.delivery_time
            output["name"] = data.user_name
            output["email"] = data.user_email
            output["mobile_self"] = data.user_mobile_self
            output["mobile_family"] = data.user_mobile_family
            output["address"] = data.user_address
            return JsonResponse(output)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    
    
# user can cancel oreder by using this fuction
def orderCancelByUser(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            if data.order_status != "successful":
                data.order_status = "cancel by user"
                data.save()
                return JsonResponse("order canceled successfully",safe = False)
            else:
                return JsonResponse("order is already successful",safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# shops can cancel oreder by using this fuction
def orderCancelByShop(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            if data.order_status != "successful":
                data.order_status = "cancel by Shop"
                data.save()
                return JsonResponse("order cancelled successfully",safe = False)
            else:
                return JsonResponse("order is already successful",safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# after delivered medicines shop can make it successfull.
def orderSuccessful(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            if data.order_status == "inprogress":
                data.order_status = "successful"
                data.save()
                return JsonResponse("order cancelled successfully",safe = False)
            else:
                return JsonResponse("order is already cancelled or successful",safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# if there is medicines unavailable then this function would be used
def orderUnvailable(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            if data.order_status == "pending":
                data.order_status = "unavailable"
                data.save()
                return JsonResponse("changes successful",safe = False)
            else:
                return JsonResponse("order is already cancelled or successful",safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# shop can provide required information to user
def orderInprogress(request):
    if request.method == 'POST':
        orderId = request.POST.get("orderId")
        price = request.POST.get("price")
        time = request.POST.get("time")
        try:
            data = medicine_orders.objects.get(order_id = orderId)
            if data.order_status == "pending" or data.order_status == "unavailable":
                data.order_status = "inprogress"
                data.price = price
                data.delivery_time = time
                data.save()
                return JsonResponse("changes successful",safe = False)
            else:
                return JsonResponse("order is already cancel or successful",safe = False)
        except ELDERLY_CARE.models.medicine_orders.DoesNotExist:
            return JsonResponse("invalid order",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)


# This function would use to find all related consultant
def searchConsultant(request):
    if request.method == 'POST':
        loc = request.POST.get("location")
        disease = request.POST.get("disease")
        gender = request.POST.get("gender")
        data = Consultant.objects.filter( 
                    Q(street_no_name = loc, speciality_field =disease, gender = gender) |
                    Q(area_name = loc, speciality_field =disease, gender = gender) |
                    Q(village_city = loc, speciality_field =disease, gender = gender) | 
                    Q(tehsil = loc, speciality_field =disease, gender = gender) |
                    Q(district = loc, speciality_field =disease, gender = gender) |
                    Q(state = loc, speciality_field =disease, gender = gender) |
                    Q(country = loc, speciality_field =disease, gender = gender) 
                )
        num=1
        consultant_list={}
        for records in data:
            consultant_list[num]=f"{records.consultant_name}, {records.speciality_field}, {records.gender}, {records.hospital_name}, {records.hospital_contact_no}, {records.street_no_name}, {records.area_name}, {records.village_city}, {records.tehsil}, {records.district}, {records.state}, {records.country}."
            num+=1
        if len(consultant_list)>0:
            return JsonResponse(consultant_list)
        else:
            return JsonResponse("no result found please provide another location or gender",safe = False)   
    else:
        return JsonResponse(" invalid method",safe = False) 
    

# this function would use to make appointment
def makeAppointment(request):
    if request.method == 'POST':
        consultantId = request.POST.get("consultantId")
        userMail = request.POST.get("userEmail")
        disease = request.POST.get("disease")
        appointmentDate = request.POST.get("appointmentDate")
        try:
            consultant_data = Consultant.objects.get(consultant_regi_id = consultantId)
            user_data = Users.objects.get(email = userMail)
            medOrderRefVar = appointments(
                        ask_appointment_date = appointmentDate,
                        consultant_id = consultantId,
                        consultant_name = consultant_data.consultant_name,
                        consultant_gender = consultant_data.gender,
                        speciality_type = consultant_data.speciality_field,
                        hospital_id = consultant_data.hospital_regi_id,
                        hospital_name = consultant_data.hospital_name,
                        hospital_contact = consultant_data.hospital_contact_no,
                        hospital_address = f"{consultant_data.street_no_name}, {consultant_data.area_name}, {consultant_data.village_city}, {consultant_data.tehsil}, {consultant_data.district}, {consultant_data.state}, {consultant_data.country}.",
                        user_name = user_data.user_name,
                        user_gender = user_data.gender,
                        illness_type = disease,
                        user_email = userMail,
                        user_mobile = user_data.mobile_self,
                        user_address = f"{user_data.home_no_name}, {user_data.street_no_name}, {user_data.area_name}, {user_data.village_city}, {user_data.tehsil}, {user_data.district}, {user_data.state}, {user_data.country}."
                    )
            medOrderRefVar.save()
            return JsonResponse("appointment successfully placed",safe = False)
        except:
            return JsonResponse("invalid credintials",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# This function would provide all appointment of the consultant
def consultantAllAppointment(request):
    if request.method == 'POST':
        consultantId = request.POST.get("consultantId") #consultantId = consultant_regi_id
        try:
            data = appointments.objects.get(consultantId = consultantId)
            output = []
            for appointment in data:
                appointment_data = {
                    "appointmentId": appointment.appointment_id,
                    "entry_date": appointment.entry_date,
                    "appointment_status": appointment.appointment_status,
                    "ask_appointment_date": appointment.ask_appointment_date,
                    "given_appointment_date": appointment.given_appointment_time,
                    "name": appointment.user_name,
                    "birth_date": appointment.user_birth_date,
                    "disease": appointment.illness_type,
                    "gender": appointment.user_gender,
                    "email": appointment.user_email,
                    "mobile_self": appointment.user_mobile,
                    "address": appointment.user_address
                }
                output.append(appointment_data)
            return JsonResponse(output, safe = False)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid credintial",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)


# This function would provide all appointment of the user
def userAllAppointment(request):
    if request.method == 'POST':
        mail = request.POST.get("email") 
        try:
            data = appointments.objects.get(email = mail)
            output = []
            for appointment in data:
                appointment_data = {
                    "appointmentId": appointment.appointment_id,
                    "entry_date": appointment.entry_date,
                    "appointment_status": appointment.appointment_status,
                    "ask_appointment_date": appointment.ask_appointment_date,
                    "given_appointment_date": appointment.given_appointment_time,
                    "consultant_id": appointment.consultant_id,
                    "consultant_name": appointment.consultant_name,
                    "gender": appointment.consultant_gender,
                    "specialist": appointment.speciality_type,
                    "hospital_id": appointment.hospital_id,
                    "hospital_name": appointment.hospital_name,
                    "hospital_contact": appointment.hospital_contact,
                    "address": appointment.hospital_address
                }
                output.append(appointment_data)
            return JsonResponse(output, safe = False)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid credintials",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# This function would provide appointment view of the consultant
def consultantAppointmentView(request):
    if request.method == 'POST':
        appointmentId = request.POST.get("appointmentId") #appointmentId = appointment_id
        try:
            data = appointments.objects.get(appointment_id = appointmentId)
            output = {}
            output["appointmentId"] = data.appointment_id
            output["entry_date"] = data.entry_date
            output["appointment_status"] = data.appointment_status
            output["ask_appointment_date"] = data.ask_appointment_date
            output["given_appointment_date"] = data.given_appointment_time
            output["name"] = data.user_name
            output["birth_date"] = data.user_birth_date
            output["disease"] = data.illness_type
            output["gender"] = data.user_gender
            output["email"] = data.user_email
            output["mobile_self"] = data.user_mobile
            output["address"] = data.user_address
            return JsonResponse(output)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid credintials",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    
# This function would provide appointment view of the user
def userAppointmentView(request):
    if request.method == 'POST':
        appointmentId = request.POST.get("appointmentId") 
        try:
            data = appointments.objects.get(appointment_id = appointmentId)
            output = {}
            output["appointmentId"] = data.appointment_id
            output["entry_date"] = data.entry_date
            output["appointment_status"] = data.appointment_status
            output["ask_appointment_date"] = data.ask_appointment_date
            output["given_appointment_date"] = data.given_appointment_time
            output["consultant_id"] = data.consultant_id
            output["consultant_name"] = data.consultant_name
            output["gender"] = data.consultant_gender
            output["specialist"] = data.speciality_type
            output["hospital_id"] = data.hospital_id
            output["hospital_name"] = data.hospital_name
            output["hospital_contact"] = data.hospital_contact
            output["address"] = data.hospital_address
            return JsonResponse(output)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid credintials",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)


# user can cancel appointment by using this fuction
def appointmentCancelByUser(request):
    if request.method == 'POST':
        appointmentId = request.POST.get("appointmentId")
        try:
            data = appointments.objects.get(appointment_id = appointmentId)
            if data.appointment_status != "successful":
                data.appointment_status = "cancel by user"
                data.save()
                return JsonResponse("appointment cancelled successfully",safe = False)
            else:
                return JsonResponse("appointment is already successful",safe = False)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid appointment",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# shops can cancel oreder by using this fuction
def orderCancelByShop(request):
    if request.method == 'POST':
        appointmentId = request.POST.get("appointmentId")
        try:
            data = appointments.objects.get(appointment_id = appointmentId)
            if data.appointment_status != "successful":
                data.appointment_status = "cancel by hospital"
                data.save()
                return JsonResponse("appointment canceld successfully",safe = False)
            else:
                return JsonResponse("appointment is already successful",safe = False)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid appointment",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# shop can provide required information to user
def scheduleAppointment(request):
    if request.method == 'POST':
        appointmentId = request.POST.get("appointmentId")
        scheduleDateTime = request.POST.get("scheduleDateTime")
        try:
            data = appointments.objects.get(appointment_id = appointmentId)
            if data.appointment_status == "pending":
                data.appointment_status = "scheduled"
                data.given_appointment_time = scheduleDateTime
                data.save()
                return JsonResponse("changes successful",safe = False)
            else:
                return JsonResponse("appointment is already cancelled or successful",safe = False)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid appointment",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)
    

# after appointment hospital can make it successful.
def appointmentSuccessful(request):
    if request.method == 'POST':
        appointmentId = request.POST.get("appointmentId")
        try:
            data = appointments.objects.get(appointment_id = appointmentId)
            if data.appointment_status == "scheduled":
                data.appointment_status = "successful"
                data.save()
                return JsonResponse("appointment successful",safe = False)
            else:
                return JsonResponse("appointment is already cancelled",safe = False)
        except ELDERLY_CARE.models.appointments.DoesNotExist:
            return JsonResponse("invalid appointment",safe = False)
    else:
        return JsonResponse(" invalid method",safe = False)