# Module
# Mehrere Python Skripte zusammenbauen
# Modul ist eine alternativer Begriff zu Python Skript

# Module importieren:
# - import <Name>
# - from <Name> import <Member>
# Jeder Import kann zusätzlich mit einem Alias versehen werden (as <Name>)

# import
# Importiert ein gesamtes Skript
# -> Funktionen, Klassen, Member (Variablen)
# WICHTIG: Wenn ein Skript importiert wird, wird es immer vollständig ausgeführt
import M000
M000.countCase("Hallo Welt")  # Print-Statements im Skript werden auch ausgeführt

import M000 as Null  # Alias
Null.countCase("Hallo Welt")

# from import
# Importiert nur bestimmte ausgewählte Member
# Bindet die importierten Member in das Skript ein; D.h. es wird kein Prefix benötigt (z.B. M000...)
# WICHTIG: Wenn ein Skript importiert wird, wird es immer vollständig ausgeführt
from M006 import halloWelt, summe, printPerson
halloWelt("Lukas")  # Kein M006. notwendig

# import *
# Beim from-Import kann auch alles importiert werden
# Spart den Prefix im Gegensatz zum regulären import
from M006 import *

################################################################################

# Der Modul Suchpfad
# Beim Import werden 4 verschiedene Pfade durchsucht:
# - Derselbe Ordner wie das jetztige Skript
# - venv/site-packages: externe Pakete
# - Bei der globalen Python Installation (AppData)
# - Unter eigens definierten Pfaden (sys.path.append)
# Wenn in den Pfaden kein Modul gefunden wird: ModuleNotFoundError
import sys
for p in sys.path:
	print(p)

sys.path.append(r"C:\Users\lk3\Desktop")
# import xyz  # xyz.py auf dem Desktop

################################################################################

# Externe Pakete
# Externe Pakete werden in venv/site-packages abgelegt

# Zwei Optionen
# In PyCharm: Python Packages

# pip
# - pip install <Name>
# - pip uninstall <Name>
# - pip list
# ...
# pip aktualisieren: py -m ensurepip --upgrade

################################################################################

# Die Main Methode
# Startpunkt des Skripts
# Beim Import wird das gesamte Skript ausgeführt
# -> keine Statements innerhalb des Skripts
# -> Nur Funktions-/Klassendefinitionen

# Wenn Code bei direkter Skriptausführung laufen soll, sollte dies innerhalb der untenstehenden if-Anweisung passieren
# Diese if-Anweisung befindet sich meistens am Ende des Skripts
if __name__ == "__main__":
	print("...")

# __name__
# Variable, welche immer verfügbar ist
# Zwei Inhalte
# - Namen des Skripts selbst (wenn es importiert wird)
# - __main__ (wenn es direkt ausgeführt wird)
print(__name__)

# Mit dedizierter Main Methode
def main():
	print("...")

if __name__ == "__main__":
	main()

################################################################################

# Packages
# In größeren Projekten werden Skripte in Unterordner abgelegt
import M007.M007b

# __init__.py
# Wird ausgeführt, wenn das Package angegriffen wird