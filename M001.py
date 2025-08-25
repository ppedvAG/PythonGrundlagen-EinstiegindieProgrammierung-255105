# Kommentare
# Alles was nach einer Raute steht, wird nicht ausgeführt
x = 5  # Eine Variable

# Variablen
# Behälter für einen Wert
# Syntax: <Name> = <Wert>
zahl = 5

# Variablen in Python haben keinen konkreten Typen
# -> der Inhalt der Variable bestimmt den Typen der Variable
zahl = 2.5

# print: Schreibt den Inhalt einer Variable in die Konsole
print(zahl)

##################################################################

# Datentypen
# int: Ganze Zahlen
# float: Kommazahlen
# str: Text
# bool: Wahr-/Falschwert

# int: Ganze Zahl
# Integer in Python können beliebig groß/klein sein
y = 55237689407562127384747325673426639412642937562357938475289435698345689432652934571290357  # int
print(y)
print(type(y))

# float: Kommazahl
# Floats in Python können beliebig groß/klein sein
f = 552376894075621273.84747325673426639412642937562357938475289435698345689432652934571290357
print(f)
print(type(f))

# str: String (Text)
# Ein String muss mit einzelnen Hochkomma (') oder doppelten Hochkomma (") umgeben sein
h = "Hallo"
w = 'Welt'
print(h)
print(w)
print(h + w)
print(type(h))

# bool: Wahr-/Falschwert
# Kann genau 2 Werte beinhalten: True oder False
t = True
b = False

# complex: Komplexe Zahlen
c = 5 + 12j  # j = mathematisches i

##################################################################

# Stringfunktionen
s = "Hallo Welt"

# Der Punkt Operator: In die Variable hineingreifen
print(s.count("l"))

# lower(), upper(): Konvertiert den gesamten string zu lowercase oder UPPERCASE
print(s.lower())
print(s.upper())

# title(), capitalize(): Erste(r) Buchstabe(n) groß, Rest klein
s.capitalize()
s.title()

# islower(), isupper(): Ist der gesamte String lowercase oder UPPERCASE?
print(s.islower())
print(s.isupper())

# len(...): Gibt die Länge einer Liste zurück
print(len(s))  # 10

##################################################################

# Index
# "An der Stelle"
# Bei einer Liste bestimmte Elemente entnehmen
# In Python fängt der Index bei 0 an
text = "Hallo Welt"

print(text[0])  # [<Zahl>]: Index

print(text[-3])  # Liste von rechts angreifen

print(text[0:5])  # Bereichsindex (von, bis) [0, 1, 2, 3, 4]

##################################################################

# Arithmetik
# Berechnungen durchführen (mit Zahlen)
z1 = 5
z2 = 8

z1 + z2  # Berechnet die Summe (temporär, z1 und z2 unverändert)
z1 += z2  # Berechnet die Summe und schreibt diese in z1 (permanent, z1 wird geändert)

print(z1 + z2)

# Modulo: Rest einer Division
print(z1 % z2)  # 1, 5R

# Potenzoperator
# X^Y
print(z1 ** 2)  # 13^2=169
print(z1 ** 0.5)  # Wurzel ziehen

# Ganzzahldivision
# X / Y = abgerundet
print(15 / 7)   # 2.142857142857143
print(15 // 7)  # 2

# Arithmetik mit Strings
hallo = "Hallo"
welt = "Welt"
print(hallo + " " + welt)

# Strings multiplizieren
print(hallo * 20)