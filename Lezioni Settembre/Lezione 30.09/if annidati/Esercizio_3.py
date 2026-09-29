#Esercizio 3. Una libreria fa uno sconto del 15% agli studenti maggiorenni (età ≥ 18) che hanno una media scolastica di almeno 8. Si controlla prima l'età, e solo se maggiorenne si controlla la media.

eta = int(input("Età? "))
media = float(input("Media scolastica? "))
prezzo = float(input("Prezzo del libro? "))

if eta >= 18:
    if media >= 8:
        prezzo = prezzo - prezzo * 0.15
        print(f"Sconto applicato! Prezzo finale: {prezzo} euro")
    else:
        print(f"Sei maggiorenne, ma la media non è sufficiente per lo sconto. Prezzo: {prezzo} euro")
else:
    print(f"Sconto riservato ai maggiorenni. Prezzo: {prezzo} euro")