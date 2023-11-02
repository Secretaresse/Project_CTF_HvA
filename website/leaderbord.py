from flask import Blueprint, render_template, session, redirect, url_for
import mysql.connector
import sys

Leaderbord = Blueprint('leaderbord', __name__)

@Leaderbord.route('/leaderbord', methods=['POST', 'GET'])
def leaderbord():
   # Create db connection
   connection = mysql.connector.connect(user='jelle', password='ditodb', host='mysql', port="3306", database='ditodb')

   cursor = connection.cursor()
   #query
   query_score = """SELECT user.username, SUM(challenge.points) as total_points
                FROM ditodb.user 
                LEFT JOIN ditodb.challenge_complete ON user.id = challenge_complete.user_id
                LEFT JOIN ditodb.challenge ON challenge_complete.challenge_id = challenge.id
                GROUP BY user.id
                ORDER BY total_points DESC LIMIT 10;"""
   
   cursor.execute(query_score)
   scores = cursor.fetchall()
   

   connection.close()
   return render_template("leaderboard.html", scores = scores)