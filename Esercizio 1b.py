anni = int(input("Inserisci gli anni di servizio "))
livello = int(input("Inserisci il tuo livelo di programmatore (livello 1 = 1), (livello 2 = 2), (livello 3 = 3) "))

if (livello == 1):
    if(anni == 1):
        print("Hai diritto ad un bonus di 100")
    elif(anni <=3):
        print("Hai diritto ad un bonus di 200")
    elif(anni <=5):
        print("Hai diritto ad un bonus di 300")
    elif(anni <=7):
        print("Hai diritto ad un bonus di 400")
    elif(anni >7):
        print("Hai diritto ad un bonus di 500")
    else:
        print("Hai inserito un livello non valido")
elif (livello == 2):
    if(anni == 1):
        print("Hai diritto ad un bonus di 200")
    elif(anni <=3):
        print("Hai diritto ad un bonus di 300")
    elif(anni <=5):
        print("Hai diritto ad un bonus di 400")
    elif(anni <=7):
        print("Hai diritto ad un bonus di 500")
    elif(anni >7):
        print("Hai diritto ad un bonus di 600")
    else:
        print("Hai inserito un livello non valido")
elif (livello == 3):
    if(anni == 1):
        print("Hai diritto ad un bonus di 200")
    elif(anni <=3):
        print("Hai diritto ad un bonus di 300")
    elif(anni <=5):
        print("Hai diritto ad un bonus di 400")
    elif(anni <=7):
        print("Hai diritto ad un bonus di 500")
    elif(anni >7):
        print("Hai diritto ad un bonus di 600")
    else:
        print("Hai inserito un livello non valido")
else:
    print("Anni inseriti non validi")