#Esercizio 5. La lavanderia self-service. Sconto del 15% se si lavano almeno 3 carichi di bucato in una volta; sconto fisso di 1 euro se si paga con l'app; sovrapprezzo fisso di 2 euro se si sceglie il lavaggio rapido; sconto ulteriore del 5% se si è iscritti al programma "cliente abituale" e si sono già fatti almeno 10 carichi questo mese. Tutti e quattro i controlli sono indipendenti tra loro e vengono eseguiti sempre, uno dopo l'altro.

carichi = int(input("Numero di carichi di bucato? "))
prezzocarico = float(input("Prezzo per carico? "))
pagamentoapp = int(input("Paghi con l'app? (1=si, 0=no) "))
lavaggiorapido = int(input("Scegli il lavaggio rapido? (1=si, 0=no) "))
clienteabituale = int(input("Sei iscritto al programma cliente abituale? (1=si, 0=no) "))
carichimensili = int(input("Quanti carichi hai già fatto questo mese? "))

totale = carichi * prezzocarico

if carichi >= 3:
    totale = totale - totale * 0.15

if pagamentoapp == 1:
    totale = totale - 1

if lavaggiorapido == 1:
    totale = totale + 2

if clienteabituale == 1 and carichimensili >= 10:
    totale = totale - totale * 0.05

print("Totale da pagare:", totale, "euro")