# Esercizio 1. Le fasce d'età. Chiedi l'età e stampa:
    #'Bambino' sotto i 13 anni
    #'Ragazzo' da 13 a 17 (13 e 17 inclusi)
    #'Adulto' da 18 a 64 (18 e 64 inclusi)
    #'Anziano' da 65 in su (65 incluso)

eta = int(input("Età: "))
if eta < 13:
    print("Bambino")
elif eta <= 17:
    print("Ragazzo")
elif eta <= 64:
    print("Adulto")
else:
    print("Anziano")