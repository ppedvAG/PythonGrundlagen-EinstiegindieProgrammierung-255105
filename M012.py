# Testing
# Während des Entwicklungsprozesses regelmäßig prüfen, ob der Code noch fehlerfrei ist
# Unittest

# Jeder Test ist ein sog. Test Case
# Ein Test Case besteht aus Python Code, welcher ein kleines Stück des Programms testet
# Tests sollten kontinuierlich ausgeführt werden (-> täglich, wöchentlich)

from unittest import TestCase
from M012b import Rechner
class RechnerTests(TestCase):  # Unsere Testklasse muss die Oberklasse TestCase haben
	# Hier werden jetzt unsere einzelnen Tests definiert (als Methoden)
	def testeAddiere(self):
		# AAA: Assign, Act, Assert
		# Assign: Variablen anlegen, Test vorbereiten
		r = Rechner()

		# Act: Code, welcher getestet werden soll, ausführen
		summe = r.addiere(1, 2)  # 3

		# Assert: Test auswerten
		self.assertEqual(3, summe)

	def testeSubtrahiere(self):
		r = Rechner()
		diff = r.subtrahiere(5, 2)
		self.assertEqual(3, diff)