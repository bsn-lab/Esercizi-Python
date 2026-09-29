colore = input("Inserisci il colore del semaforo (verde/rosso): ").lower()

if colore == "verde":
    print("Si può passare")
elif colore == "rosso":
    print("Ci si deve fermare")
else:
    print("Colore non valido. Inserire 'verde' o 'rosso'.")