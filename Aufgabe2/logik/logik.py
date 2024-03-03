def offnen_lesen():
    return open('meine_datei.txt', 'r')


def offnen_schreiben():
    return open('meine_datei.txt', 'w')


def schliessen(f):
    f.close()  #es schliesst das File
    return f


def einlesen():
    ersetzen = input('Wort zu ersetzen: ')
    ersatzwort = input('Ersatzwort: ')
    return ersetzen, ersatzwort, 0


def durchfuhren(ersetzen, ersatzwort, anzahl, f):
    inhalt = f.read() #inhalt enthilet meine Satzen
    anzahl += inhalt.count(ersetzen) #count zahlt wie viel das Wort ersetzt ist
    inhalt = inhalt.replace(ersetzen, ersatzwort) #replace ersetzt Ersezten mit Ersatzwort
    f = offnen_schreiben()
    f.write(inhalt)  #diese Funktion verandert meine_datei.txt
    return anzahl, f #es gibt wie viel das Wort ersetzt ist und die neue dateien aus


def ausdrucken(ersetzen, ersatzwort, anzahl):
    print("Ersetzt '", ersetzen, "' duch '", ersatzwort, "' an ", anzahl, " Stellen")
