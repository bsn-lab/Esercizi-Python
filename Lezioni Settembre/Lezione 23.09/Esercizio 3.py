#Dati in input le altezze in metri di due persone (chiedi all'utente il nome delle due persone), stampa quale delle due è più alta.

# Inserimento dei nomi e delle altezze da parte dell'utente
nome1 = input("Inserisci il nome della prima persona: ")
altezza1 = float(input(f"Inserisci l'altezza di {nome1} (in metri): "))

nome2 = input("Inserisci il nome della seconda persona: ")
altezza2 = float(input(f"Inserisci l'altezza di {nome2} (in metri): "))

# Confronto e stampa del risultato
if altezza1 > altezza2:
    print(f"{nome1} è più alto/a di {nome2}.")
elif altezza2 > altezza1:
    print(f"{nome2} è più alto/a di {nome1}.")
else:
    print(f"{nome1} e {nome2} hanno la stessa altezza.")