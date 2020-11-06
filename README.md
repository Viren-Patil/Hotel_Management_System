# Hotel Management System

This is a small application of a Hotel Management System having the following features:  
* **Registration and Login Page**: Any Customer can register an account and then login through the credentials
* **Home Page**: It is the Welcome Page and contains some of the pictures of our Hotel and other links.
* **Room Booking**: A form to book a room in hotel for particular dates.
* **Table Booking**: A form to book a table during your stay.
* **Payment**: Stay details with the total payable bill of the customer. 
* **Feedback**: A feedback form where customer can give rating and feedback of the hotel and their stay. 
* **Gallery**: Hotel Pictures.
* **Contact Us**: Contact Details of Hotel.
* **Customer Profile**: Personal Details of The Customer.
* **Forget Password Functionality**: Customer can Reset the password if he/she forgets it.
* **Logout Page**

## Steps to run the application:
1. Clone the github repository and cd to the folder 
2. Run _pip install -r requirements.txt_
3. Run _cd dbms\_project_
4. Run _python manage.py runserver_

## ER Diagram

<img src="Screenshots/ER.jpg" height="300">

## Relational Schema (After Normalization)

<img src="Screenshots/AfterNormalization.jpg" height="300">

## Some features of the application:-


Registration Page                   |                   Login Page
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/signup1.png" height="300">  | <img src="Screenshots/login.png" height="300">


Room Categories(1)                 |                   Room Categories(2)
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/categories1.png" height="300">     |<img src="Screenshots/categories2.png" height="300">

Book a Room                   |                   Book a Table
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/roombooking.png" height="300">     |<img src="Screenshots/tablebooking.png" height="300">

My Room Bookings                   |                   My Table Bookings
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/myroombookings1.png" height="300">     |<img src="Screenshots/mytablebookings.png" height="300">

Payment                 |                   Feedback
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/payment2.png" height="300">     |<img src="Screenshots/feedback.png" height="300">

Contact Us                 |                   Gallery
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/contactus.png" height="300">     |<img src="Screenshots/gallery1.png" height="300">

Welcome Page               |                   Logout Page
:---------------------------------:        |      :------------------------------:
<img src="Screenshots/welcome1.png" height="300">     |<img src="Screenshots/loggedout.png" height="300">

