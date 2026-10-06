# Esercizio 3. La gita di classe. Scrivi un programma che chieda quanti studenti partecipano alla gita e quanto paga ognuno, poi stampi il totale raccolto. 

studenti = int(input("Quanti studenti partecipano? "))
quota = float(input("Quota per studente: "))
totale = studenti * quota
print(f"Totale raccolto: {totale} euro")