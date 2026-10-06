# Esercizio 1. Scrivi un programma che chieda il voto di una verifica (può avere la virgola, es. 5.5). Se il voto è 6 o più stampa 'Sufficiente', altrimenti 'Insufficiente'.

voto = float(input("Voto della verifica: "))
if voto >= 6:
    print("Sufficiente")
else:
    print("Insufficiente")