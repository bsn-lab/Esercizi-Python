#Scrivi un programma che chieda la portata massima dell'ascensore (in kg) e il peso delle persone salite. Se il peso è maggiore della portata stampa Sovraccarico! , altrimenti stampa Si parte.

portata = int(input("Portata massima (kg): "))
peso = int(input("Peso delle persone (kg): "))

if peso > portata:
    print("Sovraccarico!")
else:
    print("Si parte")

