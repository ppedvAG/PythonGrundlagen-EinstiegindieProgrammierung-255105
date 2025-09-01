# Fehlerbehandlung
# Wenn ein Codestück einen Fehler wirft, stürzt das Skript ab

# zahl = int(input("Gib eine Zahl ein: "))  # Wenn keine Zahl gegeben ist, stürzt hier das Skript ab
# print(zahl)

# Fehler verhindern:
# - if-Anweisung(en)
# - try-except

# 1. if-Anweisung
# eingabe = input("Gib eine Zahl ein: ")
eingabe = "0"
zahl = 0
if eingabe.isnumeric():
	zahl = int(eingabe)
print(zahl)

# 2. try-except
try:  # Wenn das Skript hier abstürzt, stürzt es nicht ab
	# eingabe2 = int(input("Gib eine Zahl ein: "))
	eingabe2 = 0
	print(eingabe2)
except:  # Wenn das Skript abstürzen würde, wird stattdessen der except-Block ausgeführt
	print("Fehler bei der Eingabe")
# Generell sollte jeder except-Block eine spezifische Fehlermeldung abhandeln
# Der generische except-Block sollte der letzte Block

##########################################################################

# Mehrere except-Blöcke
try:
	eingabe3 = int(input("Gib eine Zahl ein: "))
	eingabe4 = int(input("Gib eine weitere Zahl ein: "))
	print(eingabe3 / eingabe4)
except ValueError:  # Spezifischer except-Block
	print("Eingabe ist keine Zahl")
except ZeroDivisionError:
	print("Eingabe kann nicht durch 0 dividiert werden")
except:
	print("Anderer Fehler")

##########################################################################

# else und finally
# else: Wird ausgeführt, wenn der Code im try-Block fehlerfrei ausgeführt wurde
# finally: Wird immer am Ende ausgeführt (egal ob Fehler oder nicht)
try:
	eingabe5 = int(input("Gib eine Zahl ein: "))
	print(eingabe5)
except:
	print("Fehlerhafte Eingabe")
else:
	print("Keine Fehler bei der Eingabe")
finally:
	print("Nach try/except")

##########################################################################

# raise
# Skript abstürzen lassen

# Warum?
# Eine Fehlerbehandlung ist von User zu User unterschiedlich
# Über den except-Block kann der User frei entscheiden, wie die Fehlerbehandlung aussehen soll
# -> print, Log, GUI, Datenbank, ...
# Interner Code kann nicht immer fehlerfrei an den User weitergegeben werden
# Der User muss sich um diese Fehler selbst kümmern

# raise ValueError("Das ist ein Fehler")  # Skript wird hier abgebrochen
# print("Wird nicht ausgeführt")

# Eigene Exception ohne extra Daten
# class CustomException(Exception):
# 	pass

# Eigene Exception mit zusätzlichen Daten
class CustomException(Exception):
	def __init__(self, msg, data):  # über __init__ ein extra Feld definieren
		super().__init__(msg)
		self.data = data

try:
	raise CustomException("Hallo", 123)
except CustomException as ce:  # as <Name>: Exceptionobjekt einen Namen geben; kann im except-Block angegriffen werden
	import traceback  # traceback: Nachverfolgung für den Programmierer, wo der Fehler aufgetreten ist
	with open("Log.txt", "w") as f:  # Traceback in ein Log schreiben
		for z in traceback.format_exception(ce):  # Traceback angreifen
			f.write(z)
	print(ce.data)  # Hier unten können die zusätzlichen Daten angegriffen werden

# Daten mitgeben über internen Error
try:
	raise ValueError("Nachricht", 123456789)
except ValueError as ve:
	print(ve.args[1])