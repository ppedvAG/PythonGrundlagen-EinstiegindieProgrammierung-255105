# Vererbung
# Definition von Basisklassen
# Diese Basisklassen können an Unterklassen vererbt werden
# Die Unterklassen übernehmen alle Felder und Methoden der Oberklasse

# Beispiel
# Oberklasse: Lebewesen
# Unterklassen: Mensch, Hund, Katze

# Oberklasse
class Lebewesen(object):
	def __init__(self, name: str, alter: int):
		self.name = name
		self.alter = alter

	def bewegen(self, distanz: int):
		return f"{self.name} bewegt sich um {distanz}m."

	def __str__(self):
		return f"{{{type(self)}, {self.name}, {self.alter}}}"

# Unterklasse
class Mensch(Lebewesen):  # Mit einem Typen in der Klammer kann eine Vererbung hergestellt werden
	# Überschreibung
	# Methode(n) aus der Oberklasse nehmen und diese neu definieren
	# -> Methode mit dem selben Namen definieren und eigenen Code eintragen
	def __init__(self, name: str, alter: int, adresse: str):
		# super: In Methoden der Oberklasse hineingreifen
		# Wird verwendet, um Methoden zu Verketten
		super().__init__(name, alter)  # Code aus Lebewesen ausführen
		self.adresse = adresse

	def bewegen(self, distanz: int):
		# Hier wird der Code aus Lebewesen überschrieben mit einer zusätzlichen Rückkopplung
		x = super().bewegen(distanz)  # x = f"{self.name} bewegt sich um {distanz}m."
		return f"Der Mensch {x}"

# Unterklasse
class Hund(Lebewesen):
	pass

# Unterklasse
class Katze(Lebewesen):
	pass

m = Mensch("Max", 33, "Zuhause")
print(m.bewegen(10))

####################################################################

# __str__
# Sog. ToString Methode
# Objekt zu einem String konvertieren
print(m)  # <__main__.Mensch object at 0x0000022108357CB0>

l = [1, 2, 3]  # Bei einem print, wird hier der Inhalt ausgegeben, und nicht Typ + Speicheradresse
print(l)

z = 5  # Bei einem print, wird hier der Inhalt ausgegeben, und nicht Typ + Speicheradresse
print(z)