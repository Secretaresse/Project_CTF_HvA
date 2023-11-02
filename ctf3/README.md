Admin CTF Challenge - Web Security - Hard
Created by: [Jelle]

Description
The Admin CTF Challenge is a hard-level challenge focused on web security. By completing this challenge, you will gain practical experience in identifying and exploiting vulnerabilities commonly found in insecure web designs.

In this challenge, you will encounter a signup page where you need to click on the terms and privacy link. A robot.txt file will be mentioned, which serves as a hint. Accessing the /robot.txt URL will reveal the content of the file, displaying the line Disallow: /users/admin/passwords.txt. By appending /users/admin/passwords.txt to the URL, you will obtain a username and password.

Username: admin
Password: uda1vx

The robot.txt file also contains an "allow" and "login" reference. Accessing the /login URL and providing the obtained username and password will grant you access to the flag, thus completing the CTF challenge. The theme of this challenge revolves around insecure design.

How to Access the Challenge
If you go to the main website create an account or login if you are already registered, there are three categories: EASY - MEDIUM - HARD. Click on the hard ctf, there is an link provided for you to click on to acces the ctf. 

Deployment
- Frontend
- The frontend of the challenge employs a html page and plain CSS design.

Backend
- The backend of the challenge is built using Flask.

Database
- The challenge uses MariaDB as the database management system.

Docker
- Docker is utilized for the deployment of the challenge, providing containerization and easy setup for running the application.

Solution
To solve the Admin CTF Challenge, follow these steps:

1. Obtain the Hint
Access the signup page.
Click on the terms and privacy link.
Take note of the mentioned robot.txt file.
2. Explore the robot.txt File
Access the /robot.txt URL.
Locate the line Disallow: /users/admin/passwords.txt.
Extract the username and password mentioned.
3. Access the Login Page
Visit the /login URL.
Enter the obtained username and password.
4. Obtain the Flag
Upon successful authentication, the flag will be displayed, indicating the completion of the CTF challenge.
Techniques Used to Solve the Challenge
Identifying and analyzing robot.txt files.
Exploiting insecure design patterns.
Extracting information from URLs.
Authentication bypass techniques.
Flag Location
- The flag is located within the /login page, accessible after successfully entering the username and password obtained from the robot.txt file.
- Username: admin
  Password: uda1vx
