from flask import Blueprint, render_template, request, redirect, url_for

Adminctf = Blueprint('adminctf', __name__)
@Adminctf.route('/Adminctf', methods=['GET', 'POST'])
def ctf3():
    if request.method == "GET":
        return render_template("ctf3.html")

    if request.method == "POST":
       return render_template("ctf3.html")