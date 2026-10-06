# Esercizio 3. Le medaglie del videogioco. Chiedi il punteggio di una partita e stampa:
    #'Nessuna medaglia' sotto 100
    #'Bronzo' da 100 a 299 (100 e 299 inclusi)
    #'Argento' da 300 a 599 (300 e 599 inclusi)
    #'Oro' da 600 in su (600 incluso)

punti = int(input("Punteggio: "))
if punti < 100:
    print("Nessuna medaglia")
elif punti <= 299:
    print("Bronzo")
elif punti <= 599:
    print("Argento")
else:
    print("Oro")