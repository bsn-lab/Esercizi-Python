# Esercizio 3. L'abbonamento del bus. Il prezzo dell'abbonamento mensile dipende dall'età:

    #sotto i 6 anni: gratis
    #da 6 a 18 anni (18 incluso): 15 €
    #da 19 a 69 anni: 35 €, ma chi è residente in città paga 32 €, e se in più paga con l'app paga 28 €
    #da 70 anni in su: 15 €

#Il programma chiede l'età, se la persona è residente (1 o 0) e se paga con l'app (1 o 2), poi stampa il prezzo.

eta = int(input("Età: "))
residente = int(input("Sei residente in città? (1 = sì, 0 = no) "))
app = int(input("Paghi con l'app? (1 = sì, 0 = no) "))

if eta < 6:
    prezzo = 0
elif eta <= 18:
    prezzo = 15
elif eta < 70:
    if residente == 1:
        if app == 1:
            prezzo = 28
        else:
            prezzo = 32
    else:
        prezzo = 35
else:
    prezzo = 15
    
print(f"Abbonamento mensile: {prezzo} euro")