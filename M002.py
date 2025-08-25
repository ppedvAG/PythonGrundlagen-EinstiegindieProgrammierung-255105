# liste
# Erlaubt, mehrere Werte in einer Variable zu speichern
# Wird vorallem bei Daten verwendet
# Duplikate erlaubt, Typen können gemischt werden, Elemente können hinzugefügt/entfernt werden, Index möglich, ...
# Wird mit [ ] definiert

liste = [1, 2, 3, 4]
print(liste)

print(len(liste))  # Anzahl der Elemente

print(liste[0])  # Einzelnes Element ausgeben

print(liste[0:2])

# Funktionen
# append(Wert): Neues Element hinzufügen
liste.append(10)
print(liste)

# pop(Index), remove(Wert): Entfernt Werte
liste.pop(3)  # Entfernt liste[3]
print(liste)

liste.remove(2)  # Sucht den gegebenen Wert und entfernt diesen
print(liste)

# sort(): Sortiert die Liste
liste.append(7)
print(liste)

liste.sort()  # Sortiert die Liste aufsteigend
print(liste)

liste.sort(reverse=True)  # Sortiert die Liste absteigend
print(liste)

# extend(Liste2): Verbindet zwei Listen
l2 = [1, 2, 3]

# Erwartung: [10, 7, 3, 1, 1, 2, 3]
liste.append(l2)
print(liste)
liste.remove(l2)

liste.extend(l2)  # Packt die Liste aus, und fügt die Elemente an
print(liste)

# Listen addieren
liste += l2  # Äquivalent zu extend
print(liste + l2)

##########################################################################

# tuple
# Funktioniert wie Liste, kann aber nicht verändert werden
# Verwendung: Ergebnisse von Funktionen
# Duplikate erlaubt, Typen können gemischt werden, Index möglich, ...
# Wird mit ( ) definiert

t = (1, 2, 3)
print(t)

print(len(t))

print(t[0])

print(t[0:2])

# Tupel verändern
# Tupel zu einer Liste konvertieren, verändern, zurückkonvertieren
t = list(t)
t.append(4)
t = tuple(t)
print(t)

##########################################################################

# range
# Bereich von X bis Y
# Nur ein Generator, zur Erstellung der Daten

# Syntax: range(X) (0-X)
# Syntax: range(X, Y) (X-Y)
# Syntax: range(X, Y, Z) (X-Y, mit Schrittgröße Z)
r = range(0, 10)
print(r)  # Output: range(0, 10)

# Wie kann ich den Generator dazu animieren, Daten zu erzeugen?
# Antwort: Iterieren
print(list(r))

print(list(range(0, 100, 5)))  # Range mit Schrittgröße

##########################################################################

# set
# Eindeutige Liste
# Verwendung: Simple Datenanalyse
# Typen können gemischt werden, Elemente können hinzugefügt/entfernt werden, ...
# Wird mit { } definiert

s = {1, 2, 3, 4}
print(s)

print(len(s))

##########################################################################

# dict
# Liste von benannten Werten
# Verwendung: Darstellung von komplexen Zuständen
# Typen können gemischt werden, Elemente können hinzugefügt/entfernt werden, Index möglich, Duplikate nicht möglich...
# Wird mit { } definiert
person = {
	"Vorname": "Max",
	"Nachname": "Mustermann",
	"Alter": 30,
	"Adresse": "Zuhause"
}

print(person)

print(person["Vorname"])  # Index muss mit einem String verwendet werden
print(person["Nachname"])  # Index muss mit einem String verwendet werden
print(person["Alter"])  # Index muss mit einem String verwendet werden
print(person["Adresse"])  # Index muss mit einem String verwendet werden

person["Hoehe"] = 180  # Neue Elemente hinzufügen
person["Alter"] = 31  # Bestehene Werte verändern

print(person.keys())
print(person.values())
print(person.items())

##########################################################################

# Konvertierungen
# Typen umwandeln
z1 = 5
z1 = float(z1)  # Typ der herauskommen soll mit dem Wert der Konvertiert werden soll in der Klammer

print(int(2.12345))  # Kommastellen abschneiden

l = [1, 2, 3]
l = tuple(l)
l = set(l)

zahl = 123
text = "Die Zahl ist: "
print(text + str(zahl))  # str und int können nicht addiert werden -> Konvertieren