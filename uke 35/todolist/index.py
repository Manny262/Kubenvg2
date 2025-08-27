todolist = ["ingenting", "gå tur"]


def printList():
    for i in todolist:
        print(i)

    
def menu():
    global run
    inputs = input('tast 1 for å se TODO-list, tast 2 for å legge til nye elementer, tast 3 for å slette elementer, tast q for å avslutte programmet:')
    if inputs == "1":
        printList()
        menu()
    elif inputs == "2":
        new_element = input('legg til en ny oppgave:')
        todolist.append(new_element)
        printList()
        menu()
    elif inputs == "3":
        for index, item in enumerate(todolist, start=1):
            print(f'{index}: {item}')
        
        Userinput = int(input('Hvilke element vil du slette?')) - 1
        
        if index[Userinput]:
            print()

    elif inputs == "q":
        print('Avslutter programmet...')
        run = False
        quit()
    
    else:
        print('Ikke gyldig alternativ, prøv igjen.')
        menu()

menu()
# def goBack():
#     Userinput = input('vil du gå tilbake til meny eller avslutte programet (ja/nei)')
#     if Userinput == "ja" or "Ja":
#         menu()
#     elif Userinput == 'nei' or 'Nei':
#         run = False
#     else:
#         print('ugyldig input')
#         goBack() 

