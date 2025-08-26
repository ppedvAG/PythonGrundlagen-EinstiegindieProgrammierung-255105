# if-Anweisung
# Führt ein Stück Code nur unter einer gegebenen Bedingung aus

x = 3
y = 5

if x > y:  # Doppelpunkt nicht vergessen
	print("x ist größer als y")  # WICHTIG: Aller Code innerhalb der if-Bedingung muss eingerückt sein
	print("Innerhalb der if")
print("Nach der if")

# elif, else: Sonst
if x > y:
	print("x größer als y")
elif x < y:
	print("x kleiner als y")
else:
	print("x gleich y")

###############################################################################

# Vergleichsoperatoren
# ==, !=   gleich, ungleich
# <, >=   kleiner, größer-gleich
# >, <=   größer, kleiner-gleich

# Logische Operatoren
# and, or, not
if x > y and x > 5:
	print("...")

# is: Speicheradressenvergleich
l1 = [1, 2, 3]
l2 = [1, 2, 3]
if l1 == l2:
	print("selber Inhalt")  # Haben beide Listen den gleichen Inhalt?
if l1 is l2:
	print("selbe Liste")  # Haben beide Listen die selbe Speicheradresse?

# in: Prüft, ob ein gegebenes Element innerhalb einer Liste vorhanden ist (Contains)
if x in [1, 2, 3]:  # Ist x gleich 1 oder 2 oder 3?
	print("...")

if x in range(10):  # Ist x zw. 0 und 9?
	print("...")

if x in l1:  # Ist der Wert hinter x in der Liste l1 enthalten?
	print("...")

###############################################################################

# Ternary Operator
# if-elif-else Bäume einzeilig darstellen
# if/elif/else und den Code innerhalb tauschen

# if x > y:
# 	print("x größer als y")
# elif x < y:
# 	print("x kleiner als y")
# else:
# 	print("x gleich y")

print("x größer als y") if x > y else print("x kleiner als y") if x < y else print("x gleich y")

print("x größer als y" if x > y else "x kleiner als y" if x < y else "x gleich y")