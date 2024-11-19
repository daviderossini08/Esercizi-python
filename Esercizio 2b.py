voto_1 = int(input("Inserisci il primo voto "))
voto_2 = int(input("Inserisci il secondo voto "))
voto_3 = int(input("Inserisci il terzo voto "))
formato = int(input("Se vuoi il risultato in decimi inserisci 1, se invece lo vuoi in centesimi inserisci 2 "))

media = (voto_1 + voto_2 + voto_3) / 3

if (formato == 1):
    print(f"La media dei voti inseriti è {media}")
elif (formato == 2):
    media = media * 100 / 10
    print(f"La media dei voti inseriti è {media}")
else:
    print("Valori inseriti non validi!!")