from flask import Blueprint, render_template, request, redirect, url_for

Cookies = Blueprint('cookiesctf', __name__)

@Cookies.route('/Cookiesctf', methods=['GET', 'POST'])
def ctf2():
    if request.method == "GET":
        return render_template("ctf2.html")

    if request.method == "POST":
       return render_template("ctf3.html")