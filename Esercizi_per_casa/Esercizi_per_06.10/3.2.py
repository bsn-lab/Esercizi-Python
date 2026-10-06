# Esercizio 2. Il vento. Chiedi la velocità del vento in km/h e stampa:
    #'Brezza leggera' sotto 20
    #'Vento moderato' da 20 a 49 (20 e 49 inclusi)
    #'Vento forte' da 50 a 89 (50 e 89 inclusi)
    #'Tempesta' da 90 in su (90 incluso)

vento = int(input("Velocità del vento (km/h): "))
if vento < 20:
    print("Brezza leggera")
elif vento <= 49:
    print("Vento moderato")
elif vento <= 89:
    print("Vento forte")
else:
    print("Tempesta")