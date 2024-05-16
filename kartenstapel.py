farbenliste = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
werteliste = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
stapel = ([])
for farbe in farbenliste:
    for wert in werteliste:
        karte = farbe, wert
        stapel.extend(karte)

print(stapel)
