# Esercizio 2. Il pieno di benzina. Scrivi un programma che chieda quanti litri di benzina metti e il prezzo al litro, poi stampi quanto devi pagare. 

litri = float(input("Quanti litri? "))
prezzo = float(input("Prezzo al litro: "))
totale = litri * prezzo
print(f"Da pagare: {totale} euro")