#Dato un importo in euro e il tasso di cambio euro-dollaro (1.15), calcola e stampa l'importo corrispondente in dollari.

importo_in_euro= int(input(f"inserisci importo in euro: "))
tasso_cambio= 1.15

totale= importo_in_euro*tasso_cambio

print(f"l'importo è di {totale} dollari")