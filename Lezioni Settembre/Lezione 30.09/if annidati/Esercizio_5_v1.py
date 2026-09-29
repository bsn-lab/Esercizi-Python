#Esercizio 5. L'ammissione al corso avanzato. Servono almeno 16 anni per essere ammessi. Chi ha almeno 16 anni viene ammesso subito se il punteggio del test è almeno 60. Se il punteggio è tra 40 e 59, conta l'esito di un eventuale colloquio. Se il punteggio è sotto i 40, non si è ammessi in nessun caso, nemmeno con un colloquio positivo. Chi ha meno di 16 anni non è mai ammesso, indipendentemente dal resto.

eta = int(input("Età? "))
punteggio = int(input("Punteggio test d'ingresso? "))
colloquio_positivo = int(input("Hai sostenuto un colloquio con esito positivo? (1=si, 0=no) "))

if eta >= 16:
    if punteggio >= 60:
        print("Ammesso al corso avanzato!")
    elif punteggio >= 40:
        if colloquio_positivo == 1:
            print("Ammesso al corso avanzato grazie al colloquio!")
        else:
            print("Non ammesso: punteggio insufficiente e colloquio non superato")
    else:
        print("Non ammesso: punteggio troppo basso, il colloquio non è nemmeno un'opzione")
else:
    print("Non ammesso: età minima 16 anni")