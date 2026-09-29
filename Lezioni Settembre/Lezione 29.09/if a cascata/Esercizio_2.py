#Esercizio 2. La pizzeria a domicilio. Se l'ordine supera i 25 euro, consegna gratuita (altrimenti 3 euro di consegna); se l'ordine supera i 50 euro, si riceve una bibita omaggio (stampalo in modo che il cassiere possa vederlo). Chiedi il totale ordine, calcola cosa si paga davvero.

totale = float(input("Totale ordine? "))

if totale <= 25:
    totale = totale + 3


if totale > 50:
    print("Hai diritto a una bibita omaggio!")

print("Totale da pagare:", totale, "euro")