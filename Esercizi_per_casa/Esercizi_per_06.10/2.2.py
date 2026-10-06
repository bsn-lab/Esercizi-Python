# Esercizio 2. La giostra. Per salire sulle montagne russe bisogna essere alti almeno 120 cm. Scrivi un programma che chieda l'altezza e stampi 'Puoi salire!' oppure 'Mi dispiace, sei troppo basso'.

altezza = int(input("Altezza in cm: "))
if altezza >= 120:
    print("Puoi salire!")
else:
    print("Mi dispiace, sei troppo basso")