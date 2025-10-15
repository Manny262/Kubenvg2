from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('master.html')

@app.route('/start')
def page1():
    list = [
        'John', 'Per', 'Anne'
    ]
    return render_template('start.html', list = list)

if __name__ == '__main__':
    app.run(debug='True')
