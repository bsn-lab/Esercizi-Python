#Esercizio 4. Il cinema. Sconto del 10% solo se si acquistano almeno 3 biglietti e si è iscritti al programma fedeltà del cinema. Le due condizioni devono valere contemporaneamente, non basta una sola.

biglietti = int(input("Numero biglietti? "))
prezzounitario = float(input("Prezzo unitario? "))
fedelta = int(input("Sei iscritto al programma fedeltà? (1=si, 0=no) "))
totale = biglietti * prezzounitario
if biglietti >= 3:
    totale = totale - totale * 0.10
if fedelta == 1:
    totale = totale - 2
print("Totale da pagare:", totale, "euro")