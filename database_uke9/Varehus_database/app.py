import os, psycopg2
from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap5
app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap5(app) 
load_dotenv()

def db_queries(query, param):
    conn = psycopg2.connect(port=os.getenv('DB_PORT'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USER'),
                            password=os.getenv('DB_PASSWORD'),)
    cur = conn.cursor()
    if param != False:
        cur.execute(query, param)     
    else: 
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
    return render_template('table_view.html', table_objects = db_queries('SELECT * from Warehouse', False), type = "Warehouses" )

@app.route('/varer', methods=['POST', 'GET'])
def get_items():
    if request.method != 'POST':
        table_objects = db_queries('SELECT * from Item', False)
    else: 
        table_objects = db_queries('SELECT * from Item WHERE warehouse_id = %s', request.form['select-warehouse'])
        
    return render_template('table_view.html', table_objects = table_objects, type = "Items", warehouses = db_queries('SELECT warehouse_id, warehouse_name from Warehouse', False))
    

