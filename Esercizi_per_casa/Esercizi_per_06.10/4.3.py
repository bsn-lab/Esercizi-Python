# Esercizio 3. Il parcheggio. Un parcheggio calcola quanto deve pagare un'auto così.

    #1. Conto di base: tariffa oraria × numero di ore.
    #2. Poi controlla queste tre regole:
        #se l'auto resta 8 ore o più, c'è uno sconto di 5 €;
        #se è un'auto grande (SUV o furgone), si pagano 4 € in più;
        #se resta parcheggiata di notte, si pagano 3 € in più.

#Il programma deve chiedere la tariffa oraria, quante ore resta l'auto, se è un'auto grande e se resta di notte (1 o 0). Alla fine stampa il totale.


tariffa = float(input("Tariffa oraria: "))
ore = int(input("Quante ore? "))
auto_grande = int(input("Auto grande (SUV o furgone)? (1 = sì, 0 = no) "))
notte = int(input("Parcheggio di notte? (1 = sì, 0 = no) "))
totale = tariffa * ore
if ore >= 8:
    totale = totale - 5
if auto_grande == 1:
    totale = totale + 4
if notte == 1:
    totale = totale + 3
print(f"Totale parcheggio: {totale} euro")