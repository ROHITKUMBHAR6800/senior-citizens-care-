"""
URL configuration for SENIOR_CITIZENS_CARE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ELDERLY_CARE import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # general urls
    path('userSignUp/', views.userRegistration),
    path('consSignUp/', views.ConsultantRegistration),
    path('medicalSignUp/', views.medicalShopRegistration),
    path('emailVerify/',views.verify_email),
    path('forpwd/',views.forgatePassword),
    path('chanpwd/',views.changePassword),
    # related to medicines order
    path('findShop/',views.searchMedicalShop),
    path('placeOrd/',views.medicinesOrder),
    path('userAllOrd/',views.userAllOrder),
    path('shopAllOrd/',views.shopAllOrder),
    path('shopOrdView/',views.shopOrderView),
    path('userOrdView/',views.userOrderView),
    path('userOrdCan/',views.orderCancelByUser),
    path('shopOrdCan/',views.orderCancelByShop),
    path('ordUnavai/',views.orderUnvailable),
    path('ordInpro/',views.orderInprogress),
    path('ordSucc/',views.orderSuccessful),
    # related to appointment
    path('findCons/',views.searchConsultant),
    path('makeAppo/',views.makeAppointment),
    path('userAllAppo/',views.userAllAppointment),
    path('consAllAppo/',views.consultantAllAppointment),
    path('consAppoView/',views.consultantAppointmentView),
    path('userAppoView/',views.userAppointmentView),
    path('userAppoCan/',views.appointmentCancelByUser),
    path('consappoCan/',views.appointmentCancelByHospital),
    path('scheAppo/',views.scheduleAppointment),
    path('appoSucc/',views.appointmentSuccessful),
    # path('/',views.),

    

]
