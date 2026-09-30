#Scrivi un programma che chieda la percentuale di batteria del telefono (un numero intero da 0 a 100) e stampi:
    #Critica se è sotto 10
    #Bassa se è da 10 a 39 (10 e 39 inclusi)
    #Media se è da 40 a 79 (40 e 79 inclusi)
    #Carica se è 80 o più (80 incluso)

batteria = int(input("Percentuale di batteria: "))

if batteria < 10:
    print("Critica")
elif batteria >= 10 and batteria <= 39:
    print("Bassa")
elif batteria >= 40 and batteria <= 79:
    print("Media")
elif batteria >= 80:
    print("Carica")