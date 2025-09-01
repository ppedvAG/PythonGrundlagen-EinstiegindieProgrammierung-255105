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

# rechner()

###############################################################

class Fahrzeug:
	def __init__(self, name: str, preis: int, maxV: int, aktV: int = 0, motorAn: bool = False):
		self.name = name
		self.preis = preis
		self.maxV = maxV
		self.aktV = aktV
		self.motorAn = motorAn

	def starteMotor(self):
		if not self.motorAn:
			self.motorAn = True
			print("Motor wurde gestartet")
		else:
			print("Motor läuft bereits")

	def stoppeMotor(self):
		if self.motorAn and self.aktV == 0:
			self.motorAn = False
			print("Motor wurde gestoppt")
		else:
			print("Motor läuft noch nicht")

	def beschleunigen(self, a: int):
		if self.aktV + a > self.maxV:
			print("Neue Geschwindigkeit würde die Maximalgeschwindigkeit überschreiten")
		elif self.aktV + a < 0:
			print("Neue Geschwindigkeit würde 0 unterschreiten")
		else:
			self.aktV += a
			print(f"Neue Geschwindigkeit: {self.aktV}")

	# def beschreibung(self):
	# 	output = f"Fahrzeug {self.name} kostet {self.preis}€ und kann maximal {self.maxV}km/h fahren."
	# 	if self.aktV > 0:
	# 		output += f" Es fährt gerade {self.aktV}km/h."
	# 	return output

	def __str__(self):
		output = f"Fahrzeug {self.name} kostet {self.preis}€ und kann maximal {self.maxV}km/h fahren."
		if self.aktV > 0:
			output += f" Es fährt gerade {self.aktV}km/h."
		return output


fzg = Fahrzeug("VW", 20000, 200, 0, False)
fzg.starteMotor()
fzg.beschleunigen(50)
fzg.beschleunigen(500)
# print(fzg.beschreibung())
fzg.beschleunigen(-40)
fzg.beschleunigen(-10)
fzg.stoppeMotor()



class PKW(Fahrzeug):
	def __init__(self, name: str, preis: int, maxV: int, kmStand: int, aktV: int = 0, motorAn: bool = False):
		super().__init__(name, preis, maxV, aktV, motorAn)
		self.kmStand = kmStand

	def einsteigen(self, anzPersonen: int):
		print(f"{anzPersonen} steigen in das Auto ein.")

	def __str__(self):
		o = super().__str__()
		o += f" Es hat einen Kilometerstand von {self.kmStand}."
		return o


class Schiff(Fahrzeug):
	def __init__(self, name: str, preis: int, maxV: int, ladung: int, aktV: int = 0, motorAn: bool = False):
		super().__init__(name, preis, maxV, aktV, motorAn)
		self.ladung = ladung

	def beladen(self, ladung: int):
		self.ladung += ladung
		print(f"Das Schiff ist mit {self.ladung} beladen.")

	def __str__(self):
		o = super().__str__()
		o += f" Es ist mit {self.ladung}kg beladen."
		return o


class Flugzeug(Fahrzeug):
	def __init__(self, name: str, preis: int, maxV: int, flughoehe: int, aktV: int = 0, motorAn: bool = False):
		super().__init__(name, preis, maxV, aktV, motorAn)
		self.flughoehe = flughoehe

	def aufsteigen(self, h: int):
		self.flughoehe += h

	def __str__(self):
		o = super().__str__()
		o += f" Es fliegt auf einer Höhe von {self.flughoehe}m."
		return o

pkw = PKW("VW", 20000, 200, kmStand=50000)
print(pkw)

schiff = Schiff("Titanic", 100_000_000, 50, ladung=50_000)
print(schiff)

flugzeug = Flugzeug("Boeing 747", 50_000_000, maxV=1000, flughoehe=10_000)
print(flugzeug)