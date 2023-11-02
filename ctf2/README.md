Coockie CTF - insecure design - medium 
Created by: Andres

Description

As you enter the page you need to log. There is a small hint on the screen about coockies. If you look into the coockies session you will find that the session is a guest session and if you change this to a different session type you will get a different outcome. In this ctf will the challanger be challanged to find is way around the coockie session to see if he can get acces to the log in data.


Deployment

Frontend:

the frontend of the website is built using HTML and CSS
the website shows a login page where you need to try and log in with the correct username and password

Backend:

the backend is implented using FLask

Database:

there is no database used for this ctf


 Solution

Step 1:
go to the coockies 

Step 2:
change the session to admin

step 3:
and there you go you have the flag

Techniques used to solve the challenge
    inspecting the elements of coockies 
    changing values in the coockies 
    and breaking through the login page using /admin

Flag location
  the flag location is after you break through the login page with /admin then you see the flag on the screen.