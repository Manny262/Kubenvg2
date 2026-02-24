import os, psycopg2
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__, template_folder='templates')
load_dotenv()

def db_queries(query):
    conn = psycopg2.connect(port=os.getenv('DB_PORT'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),)
    cur = conn.cursor()
    cur.execute(query)
    db_callback = cur.fetchall() 
    cur.close()
    conn.close()
    return db_callback
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/varehus')
def get_warehouses():
    # warehouses = db_queries('SELECT * from Warehouse') 
    return render_template('warehouses.html', warehouses = db_queries('SELECT * from Warehouse') )
@app.route('/varer')
def get_items():
    return render_template('items.html', items = db_queries('SELECT * from Item') )
    
