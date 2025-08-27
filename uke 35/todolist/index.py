todolist = ["ingenting", "gå tur"]


def printList():
    for i in todolist:
        print(i)

    
def menu():
    
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
        
        if Userinput < len(todolist):
            removed = todolist.pop(Userinput)
            print(f'"{removed}" er slettet fra listen.')
        else:
            print('Ugyldig valg.')
        menu()

    elif inputs == "q":
        print('Avslutter programmet...')
        quit()
    
    else:
        print('Ikke gyldig alternativ, prøv igjen.')
        menu()

menu()

