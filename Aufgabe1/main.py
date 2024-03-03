from Buchstaben.abc import *
from functions import *
import turtle
def Menü():
    return """
    Turtle Paint v1.0
    1.Textnachricht zeigen
    2.Neues Zeichen hinzüfugen
    """
def main():
    print(Menü())
    wahl=int(input("Ihre Wahl:"))
    if wahl==1:
        dictionar = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e, 'F': f, 'G': g, 'H': h, 'I': i, 'J': j, 'K': k,
                     'L': l, 'M': m, 'N': n, 'O': o, 'P': p, 'Q': q, 'R': r, 'S': s, 'T': t, 'U': u, 'V': v,
                     'X': x, 'Y': y, 'Z': z, '.': punkt, '?': frage, '!': ausrufe, ' ': space}
        string=input("Wort hinzufügen:")
        turt=turtle.Pen()
        for letter in string:
            idx=ord(letter)-32 #es macht die Buchstabe gross
            dictionar[chr(idx)]() #es ruft die Funktion der Buchstabe an



    elif wahl==2:
        worterbuch={} #wir bauen ein nues worterbuch
        trt = turtle.Pen()
        while True:
            lit = input("Geben Sie eine Buchstabe ein:")
            if lit in worterbuch:
                print("Die Buchstabe befindet sich in dem Wörterbuch.")
            elif lit == "":
                break
            else:
                lista = []
                steuer = input("Anweisung geben:")
                while True:
                    anweisung(steuer, trt) #es kontrolliert den TurtlePen
                    steuer = input("Anweisung geben:")
                    if steuer=="" or steuer==' ': #es stoppt
                        break
                    lista.append(steuer) #steuer wird in der Liste hinzugefugt
                worterbuch[lit]=lista #es enthalt die Anweisungen fur das Zeichnen der Buchstaben
        print_file(worterbuch) #es schreibt das Worterbuch in der Datei
main()