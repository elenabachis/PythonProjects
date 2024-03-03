from logik.logik import * #die Funktionen aus logik werden importiert sein

def menu():
    return '''
        Pfad zur Datei: meine_datei.txt
        1-Programm beginnen 
        0-Exit
    '''

def main():
    while True: #while 1
        print(menu())
        option=int(input('Wahlen Sie ein Option aus: '))
        if option == 1: #Programm beginnen
            f = offnen_lesen()
            ersetzen, ersatzwort, anzahl = einlesen() #die worter werden gelesen
            anzahl, f = durchfuhren(ersetzen, ersatzwort, anzahl, f) #die Durchfuhrung aus logik
            ausdrucken(ersetzen, ersatzwort, anzahl) #es gibt die Datei aund Anzahl aus
            f = schliessen(f) #es schlieesst die Funktion
        if option == 0: #Exit
            break



