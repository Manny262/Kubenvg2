import bcrypt 

passord = "1234".encode('utf-8')
hashed = bcrypt.hashpw(passord, bcrypt.gensalt())

print("orginalt", passord)
print("hashed", hashed)

nyttPassord = input("skriv inn et nyttpassord: ").encode('utf-8')
hashed1 = bcrypt.hashpw(nyttPassord, bcrypt.gensalt())


checkpwd = input("skriv inn passordet ditt: ").encode('utf-8')
if bcrypt.checkpw(checkpwd, hashed1):
    print("riktig passord")
else:
    print("feil passord")


