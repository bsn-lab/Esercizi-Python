# Esercizio 1. La cartoleria. Scrivi un programma che chieda quanti quaderni compri e quanto costa un quaderno, poi stampi la spesa totale. 1.

quaderni = int(input("Quanti quaderni? "))
prezzo = float(input("Prezzo di un quaderno: "))
totale = quaderni * prezzo
print(f"Spesa totale: {totale} euro")