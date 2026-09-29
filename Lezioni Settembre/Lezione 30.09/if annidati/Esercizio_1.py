#Esercizio 1. Il parco acquativo. Per accedere alla piscina degli adulti bisogna avere almeno 8 anni. Chi ha almeno 8 anni può accedere anche alla piscina profonda, ma solo se sa nuotare. Dati età e se si sa nuotare, stampa a quale piscina si può accedere.

eta = int(input("Età? "))
sa_nuotare = input("Sai nuotare? (1/0) ")
#sa_nuotare = input("Sai nuotare? (True/False) ") == "True"

if eta >= 8:
    print("Puoi accedere alla piscina degli adulti")
    if sa_nuotare:
        print("Puoi accedere anche alla piscina profonda")
    else:
        print("Ma non puoi accedere alla piscina profonda: prima impara a nuotare")
else:
    print("Puoi accedere solo alla piscina per bambini")