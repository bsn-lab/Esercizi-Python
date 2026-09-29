#Esercizio 3. L'hotel. Sconto del 10% se si prenotano almeno 3 notti; se inoltre si paga in anticipo, 5% di sconto (sul prezzo già evntualmente scontato). Chiedi prezzo a notte, numero notti, pagamento anticipato (1/0).

prezzonotte = float(input("Prezzo a notte? "))
notti = int(input("Numero di notti? "))
anticipato = int(input("Paghi in anticipo? (1=si, 0=no) "))
totale = prezzonotte * notti
if notti >= 3:
    totale = totale - totale * 0.10
if anticipato == 1:
    totale = totale - totale * 0.05
print("Totale da pagare:", totale, "euro")