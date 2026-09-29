#In una gita scolastica in montagna, ogni escursionista esperto beve 3 borracce d'acqua, ogni principiante 2 borracce, ogni accompagnatore 1 borraccia e mezza. Ogni cassa contiene 12 borracce. Dati esperti, principianti e accompagnatori, calcola quante casse servono.

numero_bottiglie= int(input(f"inserisci numero bottiglie: "))
costo= float(input(f"inserisci costo: "))

totale= numero_bottiglie*costo

print(f"il costo totale è di {totale} euro")