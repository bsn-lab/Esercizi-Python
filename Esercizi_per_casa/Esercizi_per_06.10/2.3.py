# Esercizio 3. Il salvadanaio. Scrivi un programma che chieda quanti soldi hai risparmiato e quanto costa il videogioco che vuoi. Se i risparmi bastano stampa 'Puoi comprarlo!', altrimenti 'Non ti bastano i soldi'.

risparmi = float(input("Quanto hai risparmiato? "))
prezzo = float(input("Quanto costa il videogioco? "))
if risparmi >= prezzo:
    print("Puoi comprarlo!")
else:
    print("Non ti bastano i soldi")