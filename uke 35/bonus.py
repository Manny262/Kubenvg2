import random

randomnmbr = random.randint(1,100)
Completed = False 

while Completed == False: 
    Userinput = int(input('Gjett et tall mellom 1 og 100:'))

    if Userinput == randomnmbr:
        print('Du gjettet riktig')
        Completed = True 
        break
    if Userinput > randomnmbr: 
        print('Du gjettet for høyt')
    else: 
        print('Du gjettet for lavt')