# senior-citizens-care-
This repository contains project related to elderly people, how can use this web application for  various purpose like health, fitness, entertainment etc.

All required tools, used for this project are mention in requirement.txt file.

Project initiated as "SENIOR_CITIZENS_CARE" and app also created with name "ELDERLY_CARE" with virtual environment in local system.

There are new changes in settings,in installed app confuger new app, mail settings and i am usesing MySQL database for this project.

Here models like Users means eldery people,Consultant and medicals created and this modules contain major field, it can be used for furder used.

The logic behind the medical and consultant models is that elderly people can buy medicines from their nearest shop by using this application and medicines can be delivered by that perticular shops at the home of eldery people and money would be paid at the time of delivery. They can also take any perticular consultant service and can book an appointment. They can give ratting according to their satisfaction.

Here some features like forgate password, change password api's develoded if in case anyone forgate password then they can get new password and also they can change there own password. In this case email id would be played crusial role.

New model like medicine_orders and appointment are created for user can place medicianes order and can book appointment for consultant.

Medicine orders related major function, apis and url are created. In medicine orders user can placed order of medicines and if it is not available (status given by shop after order placed) then user can cancel the order also they can view all order placed by them. Also order can be cancle by shop if it will be not available for long time and they can also change status of delivery like cancelled, unavailable, inprogress (if they have in stock then they can update price and delivery time) and successful. By default order status will be pending.
