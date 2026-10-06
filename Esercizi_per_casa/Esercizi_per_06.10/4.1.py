# Esercizio 1. Una pizzeria calcola il conto di un ordine così. Ogni bibita costa sempre 2 €: questo prezzo non si chiede all'utente, lo scrivi tu nel programma in una variabile.
    #1. Conto di base: prezzo di una pizza × numero di pizze, più numero di bibite × 2 €.
    #2. Poi controlla queste tre regole:
        #se ordini 5 pizze o più, hai uno sconto di 5 €;
        #se vuoi la consegna a domicilio, paghi 3 € in più;
        #se prendi 4 bibite o più, una è in omaggio: togli il prezzo di una bibita (−2 €).

# Il programma deve chiedere il prezzo di una pizza, quante pizze ordini, quante bibite vuoi e se vuoi la consegna (si risponde True o False usando la convenzione 1 o 0). Alla fine stampa il totale.


prezzo_bibita = 2
prezzo_pizza = float(input("Prezzo di una pizza: "))
pizze = int(input("Quante pizze? "))
bibite = int(input("Quante bibite? "))
consegna = int(input("Consegna a domicilio? (1 = sì, 0 = no) "))
totale = prezzo_pizza * pizze + bibite * prezzo_bibita
if pizze >= 5:
    totale = totale - 5
if consegna == 1:
    totale = totale + 3
if bibite >= 4:
    totale = totale - prezzo_bibita
print(f"Totale ordine: {totale} euro")