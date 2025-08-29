# Klassen und Objekten
# Erlaub die Modellierung von komplexen Zuständen/Sachverhalten/Datentypen
# Die Klasse selbst definiert nur die Struktur -> keine konkreten Werte
# Aus der Klasse können konkrete Objekte erzeugt werden -> konkrete Werte werden hier eingetragen

############## DAS GROße DATENTYPEN QUIZ ##############
# int: Ganze Zahl
# float: Kommazahl
# str: Text
# bool: Wahrheitswerte
# list: Behälter für mehrere Werte
# Person: ?
#######################################################

# Person kann nicht simpel beschrieben werden -> eigene Klasse

# Die Person Klasse
class Person:
	def __init__(self):
		"""
		docstring (Dokumentationskommentar)

		Erlaub es, Methoden/Klassen zu kommentieren

		__init__ wird bei Erzeugung des Objektes ausgeführt

		Innerhalb von __init__ werden die Felder der Klasse angelegt
		"""

		# Felder: Vorname, Nachname, Alter, Adresse
		# Diese Felder müssen hier angelegt werden
		# Syntax: self.<Name> = <Standardwert>
		self.vorname = ""
		self.nachname = ""
		self.alter = 0
		self.adresse = ""
		# Nach Erstellung des Objektes können diese Felder beschrieben werden


p = Person()  # Erstellung eines Objektes
p.vorname = "Lukas"  # Eintragen von konkreten Werten
p.nachname = "Kern"
p.alter = 27
p.adresse = "Zuhause"

p2 = Person()
p2.vorname = "Martin"

p3 = Person()
p3.vorname = "Wiebke"

# Warum?
# Wir können jetzt Personendaten repräsentieren
# z.B. Microsoft Teams; jeder Kontakt ist innerhalb der Anwendung ein Objekt
# Felder: Name, Adresse, TelNr, Email, Zeitzone, Chatverlauf, Status, ...

# z.B. Besprechungen
# Felder: Termin, Thema, Ort, Agenda, Titel, Teilnehmer, ...

##########################################################################################

# Verbesserungen Person
class PersonCool:
	def __init__(self, vorname: str, nachname: str, alter: int = -1, adresse: str = ""):
		"""
		Jetzt können hier Standardwerte über den User erzwungen werden

		Hierfür können bei self zusätzliche Parameter gegeben werden
		"""
		self.vorname = vorname
		self.nachname = nachname
		self.alter = alter
		self.adresse = adresse

	def hallo(self):
		"""
		Methode

		Funktion, welche immer mit einem Objekt zusammenhängt

		Methoden haben immer einen self Parameter

		Alle Objekte, die aus dieser Klasse erzeugt werden, haben diese Methode
		"""
		print(f"Hallo mein Name ist: {self.vorname}")


# Vorher:
# p = Person()
# p.vorname = "Lukas"
# p.nachname = "Kern"
# p.alter = 27
# p.adresse = "Zuhause"

# Nachher:
p = PersonCool("Lukas", "Kern", 27, "Zuhause")
p2 = PersonCool("", "")  # Mit optionalen Parametern auch möglich

p.hallo()  # hallo() bezieht sich hier auf das Objekt p; Output: Hallo mein Name ist: Lukas
p2.hallo()