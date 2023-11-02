from flask import Blueprint, render_template, request, redirect, url_for,session
import mysql.connector


Login = Blueprint('login', __name__)
@Login.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        connection = mysql.connector.connect(
            user='jelle', password='ditodb', host='mysql', port="3306", database='ditodb')
        
        cursor = connection.cursor()


        # Get seat number and name from form
        username = request.form['username']
        password = request.form['password']

        # Make the query
        sql = "SELECT username, password FROM user WHERE username = %s AND password = %s"
        data = (username, password)

        # Execute the query
        cursor.execute(sql, data)

        # Fetch one user
        user = cursor.fetchone()

        # Close the connection
        connection.close()

        if user:
            # Set session Username
            session['username'] = request.form['username']
            return redirect(url_for("home.home"))
    return render_template("login.html")
