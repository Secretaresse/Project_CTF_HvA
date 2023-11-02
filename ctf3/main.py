# Backend for PAD CTF level Hard
# This file is owned by Team D

from flask import Flask, redirect, request, make_response, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def signuppage():
    return render_template("signup.html")

@app.route('/policy&terms', methods=['GET'])
def policy():
    return render_template("policy.html")

@app.route('/guest', methods=['GET'])
def guest():
    return render_template("guest.html")

@app.route('/home', methods=['GET', 'POST'])
def admin():
    admincookie = request.cookies.get("cookie")
    if admincookie == "Bdkjfijfalkgigigjaskj267i9dnjkllkbjdfisl":
        return render_template("admin.html")
    else:
        return render_template("login.html")
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['usrname']
        password = request.form['passwd']

        if username == "admin" and password == "uda1vx":
            cookies = request.cookies.get("cookie")
            if not cookies or cookies == "":
                response = make_response(redirect("/home", code=303))
                random_string = "Bdkjfijfalkgigigjaskj267i9dnjkllkbjdfisl"
                response.set_cookie("cookie", random_string)
                return response

            return "DitoCTF(MfbVhOCj_mp3)"
        
            

        else:
            return render_template("login.html")
    else:
        return render_template("login.html")
    


@app.route('/robots.txt', methods=['GET'])
def robots():
    return render_template("robots.txt.html")


@app.route('/users/admin/passwords.txt', methods=['GET'])
def passwordstxt():
    return render_template("passwords.txt.html")

if __name__ == "__main__":
    # Debug allows us to detect changes and updates it
    app.run(debug=True, host="0.0.0.0", port=3300)
