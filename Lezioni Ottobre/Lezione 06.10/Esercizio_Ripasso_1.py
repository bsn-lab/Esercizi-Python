#Un gruppo di amici va al cinema. Scrivi un programma che chieda quanti biglietti servono e quanto costa un biglietto, poi stampi la spesa totale.

biglietti = int(input("Quanti biglietti? "))
prezzo = float(input("Prezzo di un biglietto: "))

totale = biglietti * prezzo

print(f"Spesa totale: {totale} euro")