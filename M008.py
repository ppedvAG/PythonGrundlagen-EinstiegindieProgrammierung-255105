# input
# Über die Konsole Eingaben empfangen
# Dem User wird eine Frage präsentiert, die Antwort wird in eine Variable geschrieben
zahl = input("Gib eine Zahl ein: ")  # Rückgabewert dieser Funktion ist immer ein String
zahl = int(zahl)  # Konvertierung notwendig
print(f"Die Zahl mal 2 ist: {zahl * 2}")

##################################################################################################

# open
# Mit externen Schnittstellen (idr. Files) interagieren (oder was auch immer)
# Open öffnet einen sog. Stream
# Der Stream stellt eine Pipeline zu der Datei dar
f = open("Output.txt", "w")
f.write("Hallo1\n")  # write schreibt den string nur in den Stream (nicht in die Datei)
f.write("Hallo2\n")  # write schreibt den string nur in den Stream (nicht in die Datei)
f.write("Hallo3")  # write schreibt den string nur in den Stream (nicht in die Datei)
f.flush()  # Schreibt den Inhalt des Streams in die Datei hinein
f.close()  # Wenn ein Stream geöffnet bleibt, kann dieser nicht angegriffen werden, bis dieser geschlossen wird

# Lesen
f2 = open("Output.txt", "r")
lines = f2.readlines()
f2.close()
print(lines)

# File.Exists
import os.path
if os.path.exists("Output.txt"):
	print("Output existiert")

from os.path import join
fullPath = join("Folder", "Output.txt")
print(fullPath)

##################################################################################################

# Das with-Statement
# Erlaubt Streams automatisch zu Schließen (am Ende des Statements)
os.remove("Output.txt")
with open("Output.txt", "w") as o:
	o.write("Hallo1\n")  # write schreibt den string nur in den Stream (nicht in die Datei)
	o.write("Hallo2\n")  # write schreibt den string nur in den Stream (nicht in die Datei)
	o.write("Hallo3")  # write schreibt den string nur in den Stream (nicht in die Datei)
# flush() und close() werden automatisch ausgeführt

##################################################################################################

# rstring
# String, welcher Escape-Sequenzen ignoriert
# Besonders nützlich bei Pfaden
pfad = "C:\\Users\\lk3\\source\\repos\\Python_Grundkurs_2025_08_25"  # Backslashes können auch Escaped werden
pfad = r"C:\Users\lk3\source\repos\Python_Grundkurs_2025_08_25"

print(r"\n\t\\")

# https://learn.microsoft.com/en-us/cpp/c-language/escape-sequences?view=msvc-170