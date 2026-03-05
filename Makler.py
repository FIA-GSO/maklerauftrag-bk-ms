#Variablen
liste_räume = []

#Funktion zur Berechnung eines Rechteckes
def Rechnung(seite_a, seite_b):
    fläche = seite_a * seite_b
    return fläche

print("---> Welcommen im Wohungsrechner <---")
print("Wieviele Räume hat die Wohnung?")
anzahl_raeume = int(input())

#For-Schleife für Anzahl der Räume
for i in range(0, anzahl_raeume):
    i = i+1

    #Werte für denn Großen Raum
    raum = input("Bezeichnung des Raumes: ")
    gwert_a = int(input("Länge des Raumes in Meter : "))
    gwert_b = int(input("Breite des Raumes in Meter: "))

    #Berechnung des Großen Raumes
    fläche_raum = Rechnung(gwert_a, gwert_b)

    while True:
        print("Ist der Raum ein Rechteck? (J)a / (N)ein")

        antwort = input()
        if antwort == "n":
            #Subrahierung des kleineren Rechteckes
            print("Geben Sie die Maße des Subrahierten Raumes an!!!")
            gwert_c = int(input("Länge des kleineren Rechteckes in Meter : "))
            gwert_d = int(input("Breite des kleineren Rechteckes in Meter: "))
            fläche_raum = fläche_raum - Rechnung(gwert_c, gwert_d)
            print(fläche_raum)
            break
        elif antwort == "j":
            print(fläche_raum)
            break
    #Liste aus Tuplen (Bezeichung, Quadratmeter)
    tuple = (raum, fläche_raum)
    liste_räume.append(tuple)

print("---> Maßheft der Wohnung <---")
for raum, anzahl in liste_räume:
    print(f"{raum}: {anzahl} Quadratmeter")

#Addierung der einzelnen Räume für Gesamtfläche
wohnung = sum(tuple[1] for tuple in liste_räume)
print(f"Die Wohung hat {wohnung} Quadratmeter.")