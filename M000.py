def maximum(*zahlen):
	m = zahlen[0]
	for i in zahlen:
		if i > m:
			m = i
	return m

# print(maximum(1,2,3,4,5,6,7,8))
# print(maximum(48,12,14,9))
# print(maximum(-5, -2, -3, -4))

def countCase(text: str):
	u = 0
	l = 0
	s = 0
	for z in text:
		if z.isupper():
			u += 1
		elif z.islower():
			l += 1
		else:
			s += 1
	print(f"Sonderzeichen: {s}, Großbuchstaben: {u}, Kleinbuchstaben: {l}")

# countCase("Das ist ein Text!")

def printTN(*namen):
	if len(namen) == 0:
		print("Keine Teilnehmer")
	elif len(namen) == 1:
		print(namen[0])
	else:
		gesamt = ""
		for tn in namen[0:-1]:
			gesamt += tn + ", "
		gesamt = gesamt.rstrip(", ")
		gesamt += " und " + namen[-1]
		print(gesamt)


# n = [str(i) for i in range(4)]
# print(n[0:len(n)-1])
# printTN(*n)

###############################################################

def file():
	path = "Output.txt"
	while True:
		eingabe = input("Gib w, r oder a ein: ")
		if eingabe not in ["w", "r", "a"]:
			print("Fehlerhafte Eingabe")
			continue

		with open(path, eingabe) as f:
			if eingabe == "r":
				from os.path import exists
				if exists(path):
					print(f.readlines())
			else:
				f.write("Erfolg")
		break

# file()

def rechner():
	while True:
		z1 = input("Gib eine Zahl ein: ")
		z2 = input("Gib eine weitere Zahl ein: ")
		if not z1.isnumeric() or not z2.isnumeric():
			print("Eine der beiden Eingaben ist nicht numerisch")
			break

		z1 = int(z1)
		z2 = int(z2)

		while True:
			op = input("Gib eine Rechenoperation ein\n1: Addition\n2: Subtraktion\n3: Multiplikation\n4: Division\n")
			if not op.isnumeric():
				continue

			match op:
				case "1": print(f"{z1} + {z2} = {z1 + z2}")
				case "2": print(f"{z1} - {z2} = {z1 - z2}")
				case "3": print(f"{z1} * {z2} = {z1 * z2}")
				case "4": print(f"{z1} / {z2} = {z1 / z2}")
				case _: continue
			break

		w = input("Wiederholen? (Enter)")
		if len(w) != 0:
			break

rechner()






