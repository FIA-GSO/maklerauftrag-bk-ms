gwert_a = 0
gwert_b = 0

def Rechnung(seite_a, seite_b):
    
    fläche = seite_a * seite_b

    return fläche


raum = input("Bezeichnung Raum: ")
gwert_a = int(input("Wert 1: "))
gwert_b = int(input("Wert 2: "))

fläche_raum = Rechnung(gwert_a, gwert_b)
print(Rechnung(gwert_a, gwert_b))

tuple_raum = (raum, fläche_raum)
print(tuple_raum)
print("Ist der Raum ein rechteck?(J)a / (N)ein")

antwort = input(" j oder n")
if antwort == "j":
    print("TOP")
elif antwort == "n":
    print("NEIN")
    gwert_c = int(input("Wert 1: "))
    gwert_d = int(input("Wert 2: "))
    fläche_raum = fläche_raum - Rechnung(gwert_c, gwert_d)
    print(fläche_raum)
