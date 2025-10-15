from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import time 
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

auth = Blueprint('auth', __name__)

def get_connection():
    load_dotenv()
    return mysql.connector.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=os.getenv('name'),
    )

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username, password, email  = request.form['username'], request.form['password'], request.form['email']
        
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()

            cursor.execute('Select id FROM Users WHERE email =', (email))
            existing = cursor.fetchone()
            if not existing:
                hashed = generate_password_hash(password)
                cursor.execute('INSERT INTO Users (username, password) Values ($1, $2)', (username, hashed))
                conn.commit()
                cursor.close()
                conn.close()
                flash('Bruker opprettet')
                time.sleep(1.75)
                return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()   
            cursor.execute('Select * From users Where email = $1', (email))
            user = cursor.fetchone()
            cursor.close()
            conn.close()

            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['email'] = user['email']
                return redirect(url_for('/'))
            else:
                flash('feil brukernavn eller passord')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))