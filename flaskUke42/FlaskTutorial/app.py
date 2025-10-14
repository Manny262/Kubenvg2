from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

class bruker(db.model):
    id= db.Column(db.Serial, primary_key=True, not_null = True)
    Fornavn = db.Column(db.string(50), not_null = True)

@app.route('/')
def hello():
    return render_template('master.html')

@app.route('/start')
def page1():
    list = bruker.query.all()
    return render_template('start.html', list = list)

if __name__ == '__main__':
    app.run(debug='True')
