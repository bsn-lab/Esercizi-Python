# Esercizio 2. Il viaggio in treno. Un'agenzia calcola il prezzo di un viaggio in treno per un gruppo così.
    #1. Conto di base: prezzo di un biglietto × numero di persone.
    #2. Poi controlla queste tre regole:
        #se viaggiano 4 persone o più, il gruppo ha uno sconto di 10 €;
        #se c'è un bagaglio extra, si pagano 5 € in più;
        #se si sceglie la prima classe, si pagano 20 € in più.

#Il programma deve chiedere il prezzo di un biglietto, quante persone viaggiano, se c'è un bagaglio extra e se si viaggia in prima classe (1 o 0). Alla fine stampa il totale.


prezzo_biglietto = float(input("Prezzo di un biglietto: "))
persone = int(input("Quante persone? "))
bagaglio = int(input("Bagaglio extra? (1 = sì, 0 = no) "))
prima_classe = int(input("Prima classe? (1 = sì, 0 = no) "))
totale = prezzo_biglietto * persone
if persone >= 4:
    totale = totale - 10
if bagaglio == True:
    totale = totale + 5
if prima_classe == 1:
    totale = totale + 20
print(f"Totale viaggio: {totale} euro")