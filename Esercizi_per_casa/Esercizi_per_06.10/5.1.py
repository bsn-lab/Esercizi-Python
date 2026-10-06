# Esercizio 1.  Le montagne russe. Per salire sulle montagne russe ci sono queste regole:
    #chi è alto meno di 120 cm non può salire;
    #chi è alto almeno 120 cm e ha 12 anni o più può salire da solo;
    #chi è alto almeno 120 cm ma ha meno di 12 anni può salire solo se è con un adulto.

#Il programma chiede l'altezza, l'età e se la persona è con un adulto (1 o 0), poi stampa uno di questi messaggi: 'Sei troppo basso', 'Puoi salire da solo', 'Puoi salire insieme all'adulto , 'Per salire devi farti accompagnare da un adulto'.

altezza = int(input("Altezza in cm: "))
eta = int(input("Età: "))
adulto = int(input("Sei con un adulto? (1 = sì, 0 = no) "))
if altezza >= 120:
    if eta >= 12:
        print("Puoi salire")
    else:
        if adulto == 1:
            print("Puoi salire con l'adulto")
        else:
            print("Devi salire con un adulto")
else:
    print("Sei troppo basso")