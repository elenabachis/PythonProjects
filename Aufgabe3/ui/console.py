from logik.logik import *


def menu():
    return ''' 
    Schere, Stein, Papier Spiel 
    1-Spiel beginnnen
    0-Spiel beenden
    '''


def main():
    while True:
        print(menu())
        option = int(input('Wahlen Sie bitte ein Option aus: '))
        if option == 1:
            f, g, h = offnen_datei() #schere=die Zeichnung von f ,etc.
            schere, stein, papier = auslesen_datei(f, g, h)
            wahlen = [schere, stein, papier] #die Liste der Zeichnungen
            anzahl_benutzer, anzahl_programm = aktuelles_spiel(wahlen, 0, 0)
            ende_spiel(anzahl_benutzer, anzahl_programm)
        if option == 0:
            break