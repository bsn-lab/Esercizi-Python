#TIPOLOGIA 1 - CALCOLI SEMPLICI

# Esercizio 1. La cartoleria. Scrivi un programma che chieda quanti quaderni compri e quanto costa un quaderno, poi stampi la spesa totale. 

# Esercizio 2. Il pieno di benzina. Scrivi un programma che chieda quanti litri di benzina metti e il prezzo al litro, poi stampi quanto devi pagare. 

# Esercizio 3. La gita di classe. Scrivi un programma che chieda quanti studenti partecipano alla gita e quanto paga ognuno, poi stampi il totale raccolto. 

# TIPOLOGIA 2 - IF/ELSE

# Esercizio 1. Scrivi un programma che chieda il voto di una verifica (può avere la virgola, es. 5.5). Se il voto è 6 o più stampa 'Sufficiente', altrimenti 'Insufficiente'.

# Esercizio 2. La giostra. Per salire sulle montagne russe bisogna essere alti almeno 120 cm. Scrivi un programma che chieda l'altezza e stampi 'Puoi salire!' oppure 'Mi dispiace, sei troppo basso'.

# Esercizio 3. Il salvadanaio. Scrivi un programma che chieda quanti soldi hai risparmiato e quanto costa il videogioco che vuoi. Se i risparmi bastano stampa 'Puoi comprarlo!', altrimenti 'Non ti bastano i soldi'.

# TIPOLOGIA 3 - IF/ELIF/ELSE

# Esercizio 1. Le fasce d'età. Chiedi l'età e stampa:
    #'Bambino' sotto i 13 anni
    #'Ragazzo' da 13 a 17 (13 e 17 inclusi)
    #'Adulto' da 18 a 64 (18 e 64 inclusi)
    #'Anziano' da 65 in su (65 incluso)

# Esercizio 2. Il vento. Chiedi la velocità del vento in km/h e stampa:
    #'Brezza leggera' sotto 20
    #'Vento moderato' da 20 a 49 (20 e 49 inclusi)
    #'Vento forte' da 50 a 89 (50 e 89 inclusi)
    #'Tempesta' da 90 in su (90 incluso)

# Esercizio 3. Le medaglie del videogioco. Chiedi il punteggio di una partita e stampa:
#'Nessuna medaglia' sotto 100
#'Bronzo' da 100 a 299 (100 e 299 inclusi)
#'Argento' da 300 a 599 (300 e 599 inclusi)
#'Oro' da 600 in su (600 incluso)

# TIPOLOGIA 4 - IF A CASCATA

    #In questi esercizi le regole vanno controllate tutte, una dopo l'altra: possono valere anche tutte insieme.

# Esercizio 1. Una pizzeria calcola il conto di un ordine così. Ogni bibita costa sempre 2 €: questo prezzo non si chiede all'utente, lo scrivi tu nel programma in una variabile.

    #1. Conto di base: prezzo di una pizza × numero di pizze, più numero di bibite × 2 €.
    #2. Poi controlla queste tre regole:
        #se ordini 5 pizze o più, hai uno sconto di 5 €;
        #se vuoi la consegna a domicilio, paghi 3 € in più;
        #se prendi 4 bibite o più, una è in omaggio: togli il prezzo di una bibita (−2 €).

# Il programma deve chiedere il prezzo di una pizza, quante pizze ordini, quante bibite vuoi e se vuoi la consegna (si risponde True o False usando la convenzione 1 o 0). Alla fine stampa il totale.

# Esercizio 2. Il viaggio in treno. Un'agenzia calcola il prezzo di un viaggio in treno per un gruppo così.

    #1. Conto di base: prezzo di un biglietto × numero di persone.
    #2. Poi controlla queste tre regole:
        #se viaggiano 4 persone o più, il gruppo ha uno sconto di 10 €;
        #se c'è un bagaglio extra, si pagano 5 € in più;
        #se si sceglie la prima classe, si pagano 20 € in più.

#Il programma deve chiedere il prezzo di un biglietto, quante persone viaggiano, se c'è un bagaglio extra e se si viaggia in prima classe (1 o 0). Alla fine stampa il totale.
 

# Esercizio 3. Il parcheggio. Un parcheggio calcola quanto deve pagare un'auto così.

    #1. Conto di base: tariffa oraria × numero di ore.
    #2. Poi controlla queste tre regole:
        #se l'auto resta 8 ore o più, c'è uno sconto di 5 €;
        #se è un'auto grande (SUV o furgone), si pagano 4 € in più;
        #se resta parcheggiata di notte, si pagano 3 € in più.

#Il programma deve chiedere la tariffa oraria, quante ore resta l'auto, se è un'auto grande e se resta di notte (1 o 0). Alla fine stampa il totale.

# TIPOLOGIA 5 - IF ANNIDATI

#Quando nel testo dell'esercizio dice 'tutti gli altri', usare Else

# Esercizio 1.  Le montagne russe. Per salire sulle montagne russe ci sono queste regole:
    #chi è alto meno di 120 cm non può salire;
    #chi è alto almeno 120 cm e ha 12 anni o più può salire da solo;
    #chi è alto almeno 120 cm ma ha meno di 12 anni può salire solo se è con un adulto.

#Il programma chiede l'altezza, l'età e se la persona è con un adulto (1 o 0), poi stampa uno di questi messaggi: 'Sei troppo basso', 'Puoi salire da solo', 'Puoi salire insieme all'adulto , 'Per salire devi farti accompagnare da un adulto'.

# Esercizio 2. La spedizione del pacco. Un corriere calcola il costo di una spedizione in base a dove va il pacco e a quanto pesa:
    #Italia - Fino a 2 kg (incluso): 5 euro - Sopra i 2 kg: 9 euro
    #Estero - Fino a 2 kg (incluso): 12 euro - Sopra i 2 kg: 20 euro 

#Il programma chiede la destinazione ( italia o estero ) e il peso in kg (può avere la virgola), poi stampa il costo.

# Esercizio 3. L'abbonamento del bus. Il prezzo dell'abbonamento mensile dipende dall'età:

    #sotto i 6 anni: gratis
    #da 6 a 18 anni (18 incluso): 15 €
    #da 19 a 69 anni: 35 €, ma chi è residente in città paga 32 €, e se in più paga con l'app paga 28 €
    #da 70 anni in su: 15 €

#Il programma chiede l'età, se la persona è residente (1 o 0) e se paga con l'app (1 o 2), poi stampa il prezzo.