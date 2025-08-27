# Funktionen
# Code wiederverwenden
# Können Parameter und/oder Rückgabewert(e) haben

# Syntax: def <Name>(<Parameter>):
#			<Body>

def hallo():
	print("Hallo Welt")

hallo()  # Ab Zeile 10 ist die Funktion verwendbar

def hallo():  # Wenn eine Funktion mit dem selben Namen angelegt wird, wie eine Funktion davor, wird die vorherige Funktion überschrieben
	print("Test")

hallo()

# Funktion mit Parameter
# Funktionen können Daten empfangen
def halloName(name):
	print(f"Hallo {name}")

halloName("Lukas")

# Funktion mit Rückgabewert
# Funktionen können Ergebnisse produzieren
# Hierfür wird das return Keyword verwendet
def addiere(x, y):
	return x + y  # return beendet die Funktion
	print(x)  # Kann nicht ausgeführt werden

zahl = addiere(3, 4)  # Der Wert, welcher bei return zurückgegeben wird, wird hier in der Variable gefangen
print(zahl)

######################################################################################

# Typempfehlungen
# Bei Parametern eine Empfehlung festlegen
# User sieht die Typen, welche empfohlen wurden

def addiere2(x: int, y: int):  # Mit :<Typ> einen Typen vorschlagen
	return x + y

print(addiere2(4, 8))
print(addiere2("Hallo", "Welt"))  # Funktioniert trotz Typempfehlung

# Was ist, wenn die Empfehlung notwendig ist?
# Lösung: Typvergleich

def addiere3(x: int, y: int):
	if type(x) == int and type(y) == int:
		return x + y
	else:
		raise TypeError("x und y müssen vom Typ int sein")

# addiere3("Hallo", "Welt")  # Absturz

# Mehrere Typempfehlungen
def addiere4(x: int | float, y: int | float) -> int | float:
	return x + y

ergebnis = addiere4(3, 4)

######################################################################################

# default Arguments
# Parameter können einen Standardwert haben
# Dieser Standardwert kann überschrieben werden
def halloWelt(name: str = "Welt"):
	print(f"Hallo {name}")

halloWelt()  # Hallo Welt
halloWelt("Martin")  # Standardwert wird überschrieben: Hallo Martin

# Verwendung: Große Funktionen mit 10+ Parametern "konfiguierbar" machen
# Beispiel: pandas.read_csv
# Diese Funktion hat ~50 Parameter; jeder Parameter dient einer Option beim Lesen von dem CSV-File
# 49 dieser Parameter werden mit einem Standardwert versehen
# Dieser kann überschrieben werden, falls notwendig
# pandas.read_csv(filepath_or_buffer, *, sep=<no_default>, delimiter=None, header='infer', names=<no_default>, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=<no_default>, skip_blank_lines=True, parse_dates=None, infer_datetime_format=<no_default>, keep_date_col=<no_default>, date_parser=<no_default>, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', delim_whitespace=<no_default>, low_memory=True, memory_map=False, float_precision=None, storage_options=None, dtype_backend=<no_default>)

def printPerson(vorname = "", nachname = "", alter = 0, adresse = ""):
	print("...")

# Bei optionalen Parametern können per Gleich-Syntax die Parameter spezifisch angesprochen werden
printPerson(nachname="Mustermann", adresse="Zuhause")
printPerson(alter=30)
printPerson(vorname="Max", nachname="Mustermann")

######################################################################################

# Arbitrary Arguments
# Beliebig viele Parameter bei einem Parameter einsetzen
def summe(*numbers):  # Innerhalb der Funktion ist der numbers-Parameter ein Tupel
	s = 0
	for n in numbers:
		s += n
	return s

summe(1, 2, 3)
summe(1, 2)
summe(1)
summe()  # Beliebig viele Parameter möglich (0-∞)

# Arbitrary Keyword Arguments
# Beliebig viele Parameter bei einem Parameter einsetzen
# Unterschied zu *args: Jeder Parameter hat einen Namen (Schlüssel)
def printTeilnehmer(**tn):
	print(tn)
	for kv in tn.items():
		print(f"{kv[0]}: {kv[1]}")

printTeilnehmer(Trainer="Lukas", T1="Martin", T2="Wiebke")

######################################################################################

# Unpacking Operatoren
# Listen in ihre Einzelteile zu zerlegen
l = [1, 2, 3, 4]
# summe(l)  # Funktioniert nicht, weil hier die Liste als gesamtes bei *numbers eingetragen wird
print(summe(*l))

# In Variablen aufteilen
a, *b, c = l  # Falls die Liste zu viele Werte hat, werden die überschüssigen Werte in b gefangen
print(a)
print(b)
print(c)

# Unpacking mit dict
person = {
	"Vorname": "Max",
	"Nachname": "Mustermann",
	"Alter": 30,
	"Adresse": "Zuhause"
}

printTeilnehmer(**person)