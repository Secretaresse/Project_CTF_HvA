from flask import Blueprint, render_template, request, redirect, url_for, session, g
import mysql.connector


Panda = Blueprint('pandactf', __name__)
@Panda.route('/pandactf', methods=['GET', 'POST'])
def ctf1():
    if request.method == "GET":
        return render_template("ctf1.html")

    if request.method == "POST":
        return render_template("ctf1.html")
    

@Panda.route('/submitflag', methods=['GET', 'POST'])
def submitflag():
    if 'username' not in session:
        return redirect(url_for("login.login"))
    
    if request.method == "POST":
        flag = request.form['flag']
        username = session['username']

        connection = mysql.connector.connect(
            user='jelle', password='ditodb', host='mysql', port="3306", database='ditodb')

        cursor = connection.cursor()

        # Make the query
        sql = "SELECT challenge_id from flag WHERE flag = %s"
        data = (flag, )

        # Execute the query
        cursor.execute(sql, data)

        # Fetch one user
        challenge_id = cursor.fetchone()

        # Make the query
        sql = "SELECT id from user WHERE username = %s"
        data = (username, )

        # Execute the query
        cursor.execute(sql, data)

        # Fetch one user
        user_id = cursor.fetchone()


        if challenge_id and user_id:
            query = "INSERT INTO challenge_complete VALUES (%s, %s);"
            param = (user_id[0], challenge_id[0])
            cursor.execute(query, param)
            connection.commit()
            g.msg = f"You solved challenge {challenge_id[0]}"
        
        else:
            g.msg = f"Wrong Flag"
        # Close the connection
        connection.close()
    return render_template("submit_flag.html")
