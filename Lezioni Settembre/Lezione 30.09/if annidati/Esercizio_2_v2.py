#Esercizio 2. Il prestito in biblioteca. Un libro si può prendere in prestito solo se è disponibile. Se è disponibile, si controlla anche se l'utente ha altri libri in ritardo: in tal caso il prestito viene comunque negato.

disponibile = int(input("Il libro è disponibile? (1=si, 0=no) "))

if disponibile:
    libri_in_ritardo = int(input("Hai libri in ritardo? (1=si, 0=no) "))
    if libri_in_ritardo:
        print("Prestito negato: hai libri in ritardo da restituire")
    else:
        print("Prestito concesso!")
else:
    print("Il libro non è disponibile")