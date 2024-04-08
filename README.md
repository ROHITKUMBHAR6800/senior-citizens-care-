Senior Citizens Care
Senior Citizens Care is a web application built with Django to facilitate the management of appointments, medical orders, and user profiles for senior citizens, consultants, and medical shops.

Features
User Management: Allows senior citizens to create profiles, schedule appointments with consultants, and place medical orders.
Consultant Dashboard: Enables consultants to manage appointments, view patient details, and update appointment status.
Medical Shop Interface: Provides a platform for medical shops to receive and process medical orders placed by users.

Installation
Clone the repository:
git clone https://github.com/ROHITKUMBHAR6800/senior-citizens-care-.git

Install dependencies:
cd senior-citizens-care
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver
Access the application at http://localhost:8000.

Configuration
Database: Senior Citizens Care uses Django's default SQLite database for development. For production, configure a more robust database like PostgreSQL or MySQL.
Time Zone: The application uses UTC time zone by default. To change it to Indian time zone, modify the TIME_ZONE setting in settings.py to 'Asia/Kolkata'.
Internationalization: The application supports English language by default. For internationalization, follow Django's Internationalization documentation.

Usage
User Registration: Users can register on the platform by providing their details such as email, name, birth date, gender, and address.
Appointment Scheduling: Senior citizens can schedule appointments with consultants specifying their illness type and preferred date.
Medical Orders: Users can place medical orders specifying the required items, quantity, and delivery details.
Consultant Management: Consultants can manage appointments, view patient details, and update appointment status.
Medical Shop Interface: Medical shops can process incoming medical orders, update order status, and manage inventory.


# senior-citizens-care-
This repository contains project related to elderly people, how can use this web application for  various purpose like health, fitness, entertainment etc.

All required tools, used for this project are mention in requirement.txt file.

Project initiated as "SENIOR_CITIZENS_CARE" and app also created with name "ELDERLY_CARE" with virtual environment in local system.

There are new changes in settings,in installed app confuger new app, mail settings and i am usesing MySQL database for this project.

Here models like Users means eldery people,Consultant and medicals created and this modules contain major field, it can be used for furder used.

The logic behind the medical and consultant models is that elderly people can buy medicines from their nearest shop by using this application and medicines can be delivered by that perticular shops at the home of eldery people and money would be paid at the time of delivery. They can also take any perticular consultant service and can book an appointment. They can give ratting according to their satisfaction.

Here some features like forgate password, change password api's develoded if in case anyone forgate password then they can get new password and also they can change there own password. In this case email id would be played crusial role.

New model like medicine_orders and appointments are created for user can place medicianes order and can book appointment for consultant.

Medicine orders related major function, apis and url are created. In medicine orders user can placed order of medicines and if it is not available (status given by shop after order placed) then user can cancel the order also they can view all order placed by them. Also order can be cancle by shop if it will be not available for long time and they can also change status of delivery like cancelled, unavailable, inprogress (if they have in stock then they can update price and delivery time) and successful. By default order status will be pending.

Appointment related major function, apis and url are created. In appointment user can make appointment and  user can cancel the appointment also they can view all appointment make by them. Also appointment can be cancle by hospital if consultant will be not available for long time and they can also change status of appointment like cancelled, scheduled (if consultant is available then they can update appointment date-time) and successful. By default appointment status will be pending.
