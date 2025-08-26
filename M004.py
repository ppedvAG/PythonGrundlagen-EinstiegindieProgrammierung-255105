# Schleifen
# Code mehrmals ausführen

# while-Schleife
# Enthält eine Bedingung, Schleife läuft bis die Bedingung false ist
a = 0
b = 10
while a < b:
	print(a)
	a += 1

# break und continue
# break: Beendet die Schleife
a = 0
while a < b:
	if a == 5:
		break
	print(a)
	a += 1

# continue: Springe zum Schleifenkopf zurück (Überspringe allen Code danach)
a = 0
while a < b:
	a += 1
	if a == 5:
		continue
	print(a)

# Endlosschleife
while 1:
	if a > 0:
		break

# else bei Schleifen: Führe Code nach der Schleife aus, wenn die Schleife erfolgreich abläuft (ohne break)
while a < b:
	print("...")
else:
	print("Ohne break beendet")

######################################################################################

# for-Schleife
# Schleife, welche immer über eine Collection iteriert
liste = [1, 2, 3, 4, 5]
for x in liste:  # x: Derzeitiges Element
	print(x)

for x in range(10):  # Klassische for-Schleife (int i = 0; i < 10; i++)
	print(x)

for x in "Hallo Welt":  # Strings sind auch Listen
	print(x)

######################################################################################

# fstring
# Formatted String
# Code in Strings einbetten
zahl = 10
# output = "Die Zahl ist: " + zahl  # TypeError: can only concatenate str (not "int") to str
# output = "Die Zahl ist: " + str(zahl)
output = f"Die Zahl ist: {zahl}"
print(output)

for i in range(10):
	print(f"Die Zahl ist: {i}")
	print(f"Die Zahl hoch 2 ist: {i ** 2}")
	print(f"{i}^2={i ** 2}")