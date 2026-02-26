gwert_a = 0
gwert_b = 0

def Rechnung(seite_a, seite_b):
    
    fläche = seite_a * seite_b

    return fläche

wert_a = int(input("Wert 1: "))
wert_b = int(input("Wert 2: "))

print(Rechnung(gwert_a, gwert_b))

print("Ist der Raum ein rechteck?(J)a / (N)ein")

if input() == "j":
    print("TOP")
elif input() == "n":
    print("NEIN")
