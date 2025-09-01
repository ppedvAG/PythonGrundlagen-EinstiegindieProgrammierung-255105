# Lambda
# Sogenannte Anonyme Funktionen
# Funktion, welche direkt in eine Variable geschrieben wird, mit der Lambda-Syntax
# Benötigt kein def

def hallo():
	print("Hallo Welt")

hallo()

# Jede Funktion ist ein Objekt
# Mit def wird eine Variable angelegt, mit einem Funktionszeiger
hw = lambda: print("Hallo Welt")
hw()

# Funktion == Objekt
print(hallo)  # Funktionszeiger: <function hallo at 0x000001B769AEF240>

#########################################################

# Funktionen anonym definieren (ohne def) mithilfe von Lambda
# Syntax: lambda <Par1>, <Par2>, ...: <Body>

f = lambda x, y: x + y  # Kein return notwendig
summe = f(3, 4)
print(summe)

f2 = lambda x, y: print(f"{x} + {y} = {x + y}")
f2(3, 5)

# Sinn?
# Funktionen, die einen Funktionszeiger als Parameter erfordern
# z.B. Command in der GUI (Button)


# filter und map

# filter
# Funktion, um eine Liste zu filtern
# Benötigt einen Funktionszeiger und eine Liste
l = [1, 2, 3, 4, 5]

def teilbarDurch2(x):
	return x % 2 == 0

x = filter(teilbarDurch2, l)

y = filter(lambda x: x % 2 == 0, l)  # selbiges wie oben, aber anonym

print(list(x))  # Nur ein Generator (wie Range)
print(list(y))  # Die Daten werden erst erzeugt, wenn der Generator verwendet wird


# map
# Funktion, welche jedes Element einer Liste in eine neue Form umwandelt
# Benötigt einen Funktionszeiger und eine Liste

z = map(lambda x: x ** 2, l)

print(list(z))