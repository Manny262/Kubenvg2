from flask import Flask, request, session,redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)
limiter.init_app(app)


@app.route('/')
def index():
    return '''
    <h1>Innlogging</h1>
    <form method="POST" action="/login">
        <p>Brukernavn: <input type="text" name="brukernavn" /></p>
        <p>Passord: <input type="password" name="passord" /></p>
        <button type="submit">Logg inn</button>
    </form>
    '''

# OPPGAVE: Lag en route for '/login' som:
# 1. Bruker riktig metode (post eller get) for login 
# 2. Henter brukernavn og passord fra skjemaet
# 3. Sjekker om brukernavn og passord er riktig
# 4. Hvis riktig: Vis "Velkommen, [brukernavn]!" med link tilbake til "/"
# 5. Hvis feil: Vis "Feil brukernavn eller passord" med link til "/"
#
# Tips: Du kan selv bestemme hvilket brukernavn og passord som skal være riktig

# Skriv koden din her:

load_dotenv()
hashedPW = generate_password_hash(os.getenv('user_password'))
app.secret_key = os.getenv("secret_key")


@app.route('/home')
def home():
    if 'username' in session:
        return f'<h1>Velkommen, {session['username']}!</h1> <br> <a href="/logout">Log ut</a>'
    else:
        return '<h1>Du er ikke logget inn</h1> <br> <a href="/">Tilbake</a>'

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def check():
    formUserName = request.form['brukernavn']
    formPW = request.form['passord']
    if os.getenv('user_username') != formUserName or check_password_hash(hashedPW, formPW) != True :
            return f'<h1>Feil brukernavn eller passord</h1> <br> <a href="/">Tilbake</a>'
    else:
            session['username'] = formUserName
            return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)