import psycopg2
import os
from dotenv import load_dotenv

# Last inn miljøvariabler fra .env
load_dotenv()

# Funksjon for å utføre usikker SQL-spørring
def vulnerable_query():
    connection = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    cursor = connection.cursor()

    # Få input fra brukeren
    brukernavn = input("Skriv inn brukernavn: ")

    # Usikker SQL-spørring (sårbar for SQL-injeksjon)
    query = f"SELECT * FROM brukere WHERE brukernavn = '{brukernavn}'" 
    cursor.execute(query)

    # Hente resultat
    resultater = cursor.fetchall()
    if resultater:
        print("Bruker funnet:", resultater)
    else:
        print("Ingen brukere funnet.")

    connection.close()

# Funksjon for å utføre sikker SQL-spørring med parameterisering
def secure_query():
    connection = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    cursor = connection.cursor()

    # Få input fra brukeren
    brukernavn = input("Skriv inn brukernavn: ")

    # Sikker SQL-spørring med parameterisering, merk %s
    query = "SELECT * FROM brukere WHERE brukernavn = %s"
    cursor.execute(query, (brukernavn,))

    # Hente resultat
    resultater = cursor.fetchall()
    if resultater:
        print("Bruker funnet:", resultater)
    else:
        print("Ingen brukere funnet.")

    connection.close()

if __name__ == "__main__": # dette kjører når du kjører .py-filen:
    print("\nVelg type spørring:")
    print("1. Sårbar SQL-spørring (SQLi)")
    print("2. Sikker SQL-spørring (parameterisering)")

    valg = input("Skriv inn 1 eller 2: ")

    if valg == "1":
        vulnerable_query()
    elif valg == "2":
        secure_query()
    else:
        print("Ugyldig valg.")