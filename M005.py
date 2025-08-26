# List Comprehension
# Erstellung von Listen über eine konkrete Syntax

# Ohne LC
zahlen = []
for i in range(10):
	zahlen.append(i)
print(zahlen)

# Mit LC
zahlenLC = [i for i in range(10)]  # Schleife in die Listenklammern eintragen -> Laufvariable (hier i) vorne anhängen
print(zahlenLC)

# LC mit if-Bedingung
# Ohne LC
zahlenIf = []
for i in range(100):
	if i % 5 == 0:
		zahlenIf.append(i)
print(zahlenIf)

# Mit LC
zahlenIfLC = [i for i in range(100) if i % 5 == 0]
print(zahlenIfLC)

# LC mit anderem Ergebnis
# Ohne LC
zahlen0komma1 = []
for i in range(100):
	zahlen0komma1.append(i / 10)
print(zahlen0komma1)

# Mit LC
zahlen0komma1LC = [i / 10 for i in range(100)]
print(zahlen0komma1LC)

# LC mit verschachtelter Schleife
# Ohne LC
einMalEins = []
for x in range(1, 11):
	for y in range(1, 11):
		einMalEins.append(f"{x}x{y}={x*y}")
print(einMalEins)

# Mit LC
einMalEinsLC = [f"{x}x{y}={x*y}" for x in range(1, 11) for y in range(1, 11)]
print(einMalEinsLC)

# LC mit Ternary Operator
# Ohne LC
fizzBuzz = []
for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		fizzBuzz.append("FizzBuzz")
	elif x % 3 == 0:
		fizzBuzz.append("Fizz")
	elif x % 5 == 0:
		fizzBuzz.append("Buzz")
	else:
		fizzBuzz.append(x)
print(fizzBuzz)

# Mit LC
fizzBuzzLC = ["FizzBuzz" if x % 3 == 0 and x % 5 == 0 \
				  else "Fizz" if x % 3 == 0 \
				  else "Buzz" if x % 5 == 0 \
				  else x for x in range(1, 101)]
print(fizzBuzzLC)