print("Devi inserire i metri dei 5 lanci che l'atleta ha a disposizione se il lancio dovesse essere nullo dovrai inserire 0")

lanci_validi = 0
tot_metri = 0

l1 = int(input("Inserisci il primo lancio"))
if (l1 > 0):
    lanci_validi = lanci_validi + 1

l2 = int(input("Inserisci il secondo lancio"))
if (l2 > 0):
    lanci_validi = lanci_validi + 1

l3 = int(input("Inserisci il terzo lancio"))
if (l3 > 0):
    lanci_validi = lanci_validi + 1
    tot_metri = tot_metri + l3

l4 = int(input("Inserisci il quarto lancio"))
if (l4 > 0):
    lanci_validi = lanci_validi + 1

l5 = int(input("Inserisci il quinto lancio"))
if (l1 > 0):
    lanci_validi = lanci_validi + 1
    
print(f"La media dei lanci è {lanci_validi}")