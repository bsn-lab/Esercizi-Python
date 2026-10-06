# Esercizio 2. La spedizione del pacco. Un corriere calcola il costo di una spedizione in base a dove va il pacco e a quanto pesa:
    #Italia - Fino a 2 kg (incluso): 5 euro - Sopra i 2 kg: 9 euro
    #Estero - Fino a 2 kg (incluso): 12 euro - Sopra i 2 kg: 20 euro 

#Il programma chiede la destinazione ( italia o estero ) e il peso in kg (può avere la virgola), poi stampa il costo.

destinazione = input("Destinazione? (italia/estero) ")
peso = float(input("Peso del pacco (kg): "))
if destinazione == "italia":
    if peso <= 2:
        prezzo = 5
    else:
        prezzo = 9
else:
    if peso <= 2:
        prezzo = 12
    else:
        prezzo = 20

print(f"Costo spedizione: {prezzo} euro")