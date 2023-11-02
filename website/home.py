from flask import Blueprint, render_template, request, redirect, url_for


Home = Blueprint('home', __name__)

@Home.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("main.html")