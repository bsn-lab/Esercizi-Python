#Esercizio 4. Il torneo di calcetto. Una squadra gioca solo se ha almeno 5 giocatori presenti. Se ne ha almeno 5, si controlla se c'è il capitano; se non c'è, deve esserci almeno il vice-capitano per poter comunque giocare.

giocatori = int(input("Numero giocatori presenti? "))

if giocatori >= 5:
    capitano_presente = int(input("Il capitano è presente? (1=si, 0=no) "))
    if capitano_presente == 1:
        print("Squadra pronta: si gioca!")
    else:
        vice_presente = int(input("Il vice-capitano è presente? (1=si, 0=no) "))
        if vice_presente == 1:
            print("Il capitano non c'è, ma il vice può guidare la squadra: si gioca!")
        else:
            print("Né capitano né vice presenti: la squadra non può giocare")
else:
    print("Giocatori insufficienti: la partita è rinviata")