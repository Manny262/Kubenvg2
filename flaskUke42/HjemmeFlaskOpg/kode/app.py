"""
Enkel to-do app med Flask + MariaDB. Les readme.md før du begynner.
"""

from flask import Flask, render_template, request, redirect, session, jsonify, url_for, Blueprint
import mysql.connector
from mysql.connector import Error


from auth import auth 
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')
app.register_blueprint(auth)

def get_connection():
    load_dotenv()
    return mysql.connector.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),
        database=os.getenv('name'),
    )

def create_table():
    try:
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()  # hva er en 'cursor'?
            # hva gjør denne koden? ⬇
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email varchar(100) unique not null,
                    username varchar(50) not null,
                    password varchar(255) not null,
                    created_at timestamp default CURRENT_TIMESTAMP
                );
                           
                CREATE TABLE IF NOT EXISTS tasks (
                    TaskID INT AUTO_INCREMENT PRIMARY KEY,
                    task VARCHAR(255) NOT NULL,
                    UserID INT,
                    Foreign key (UserID) References Users(id)    
                )
                
            ''')

            conn.commit()
            cursor.close()
            conn.close()
    except Error as e:
        print(f"Feil under opprettelse av tabell: {e}")

create_table() 

@app.route('/')  # når kjører denne routen?
def index():
    if 'user_id' not in session:
        return render_template('login.html')
    else:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT task FROM tasks Where UserID = $1', (session['user_id']))  
            tasks = cursor.fetchall()              
            conn.close()
            return render_template('main.html', tasks=tasks) # hva gjør denne linjen? Hva er tasks?
        except Error as e:
            return "Kunne ikke koble til databasen."    

@app.route('/registerSite')
def registerSite():
    return render_template('register.html')


@app.route('/add', methods=['POST'])  # når kjører denne routen?
def add_task():
    task = request.form['task']  # hva er request.form['task']?

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
        conn.commit()
    except Error as e:
        print(f"Feil under lagring av oppgave: {e}")
    finally:
        conn.close()

    return redirect('/') # hva skjer hvis du fjerner denne linjen?

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)