#Esercizio 1: Sconto del 5% se la spesa supera i 300 euro; se si ha la carta fedeltà, ulteriore 3% sul totale già eventualmente scontato. Chiedi prezzo unitario, quantità, carta fedeltà (1/0).

prezzo = float(input("Prezzo unitario? "))
quantita = int(input("Quantità? "))
fedelta = int(input("Hai la carta fedeltà? (1=si, 0=no) "))
totale = prezzo * quantita
if totale > 300:
    totale = totale - totale * 0.05
if fedelta == 1:
    totale = totale - totale * 0.03
print("Totale da pagare:", totale, "euro")