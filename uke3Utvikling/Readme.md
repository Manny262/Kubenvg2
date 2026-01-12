# 4-innlogging_oppgave

- login skjema som bruker POST-method

## Ekstra som er lagt til for sikkkerhet:
- Werkzeug.security for hashing av passord
- Flask_limiter for å gi beskyttelse mot brute force attacks 
- Secret-key for å kryptere og signere session-coockies, og kan brukes ved CSRF-beskyttelse (Flask-WTF)
- Brukernavn og passord er lagret i .env fil som er lagt til i gitignore (env fil blir likke lastet opp til github)

# Brukerveiledning:

1. Opprett viruelt miljø:

cd inn i UKE3UTVIKLING
```bash 
cd UKE3UTVIKLING
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

2. Opprett .env fil:

```env
user_username = [Ditt-brukernavn]
user_password = [Ditt-passord]
secret_key=[Ditt-Secret-Key-Passord]
```

3. Start server:
```bash
python .\4-innlogging_oppgave.py
```

