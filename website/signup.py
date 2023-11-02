
from flask import Blueprint, render_template, request, redirect, url_for, g
import mysql.connector

Signup = Blueprint('signup', __name__)

@Signup.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method == 'POST':
        connection = mysql.connector.connect(
            user='jelle', password='ditodb', host='mysql', port="3306", database='ditodb')
        
        cursor = connection.cursor()

        username = request.form['username']
        password = request.form['password']

        sql_check = "SELECT username FROM user WHERE username = %s"
        usertocheck = (username,)

        cursor.execute(sql_check, usertocheck)

        user = cursor.fetchone()

        if not user:
            sql_insert_user = "INSERT INTO user (username, password) VALUE (%s,%s)"
            user_data = (username, password)
            cursor.execute(sql_insert_user, user_data)
            connection.commit()
            return redirect (url_for("login.login"))
        
        else:
            g.msg = "Deze gebruiker bestaat al!"

        connection.close()
        
    return render_template("signup.html")


