import random


def offnen_datei():
    return open('schere.txt', 'r'), open('stein.txt', 'r'), open('papier.txt', 'r')


def auslesen_datei(f, g, h):
    return f.read(), g.read(), h.read()

def schliessen(f,g,h):
    return f.close(),g.close(),h.close()

def wahl():
    benutzer = input("Wahlen Sie eine aus: \n(Schere, Stein oder Papier): ")
    return benutzer


def auswahlen(benutzer, wahlen):
    benutzer=benutzer.lower()
    if benutzer == 'schere':
        return wahlen[0]
    if benutzer == 'stein':
        return wahlen[1]
    if benutzer == 'papier':
        return wahlen[2]


def punktzahl(benutzer, programm, wahlen, anzahl_benutzer, anzahl_programm):
    if benutzer == 'schere':
        if programm == wahlen[0]:
            anzahl_benutzer = anzahl_benutzer
            anzahl_programm = anzahl_programm
        if programm == wahlen[1]:
            anzahl_programm += 1
        if programm == wahlen[2]:
            anzahl_benutzer += 1
    elif benutzer == 'stein':
        if programm == wahlen[0]:
            anzahl_benutzer += 1
        if programm == wahlen[1]:
            anzahl_benutzer = anzahl_benutzer
            anzahl_programm = anzahl_programm
        if programm == wahlen[2]:
            anzahl_programm += 1
    elif benutzer == 'papier':
        if programm == wahlen[0]:
            anzahl_programm += 1
        if programm == wahlen[1]:
            anzahl_benutzer += 1
        if programm == wahlen[2]:
            anzahl_benutzer = anzahl_benutzer
            anzahl_programm = anzahl_programm
    return anzahl_benutzer, anzahl_programm


def ende_spiel(anzahl_benutzer, anzahl_programm):
    print('Ende des Spieles.\nDie Punktazahlen sind: \nBenutzer= ', anzahl_benutzer, '\nComputer= ', anzahl_programm)
    if anzahl_benutzer < anzahl_programm:
        print('Computer hat gewonnen')
    elif anzahl_benutzer > anzahl_programm:
        print('Benutzer hat gewonnen')
    else:
        print('Die Ergebnisse sind gleich')


def aktuelles_spiel(wahlen, anzahl_benutzer, anzahl_programm):
    for i in range(3):
        benutzer = wahl()
        programm = random.choice(wahlen)
        print(auswahlen(benutzer, wahlen))
        print(programm)
        anzahl_benutzer, anzahl_programm = punktzahl(benutzer, programm, wahlen, anzahl_benutzer, anzahl_programm)
    return anzahl_benutzer, anzahl_programm

wahlen=['schere','stein','papier']