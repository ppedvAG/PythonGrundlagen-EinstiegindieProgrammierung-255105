def maximum(*zahlen):
	m = zahlen[0]
	for i in zahlen:
		if i > m:
			m = i
	return m

print(maximum(1,2,3,4,5,6,7,8))
print(maximum(48,12,14,9))
print(maximum(-5, -2, -3, -4))

def countCase(text: str):
	u = 0
	l = 0
	s = 0
	for z in text:
		if z.isupper():
			u += 1
		elif z.islower():
			l += 1
		else:
			s += 1
	print(f"Sonderzeichen: {s}, Großbuchstaben: {u}, Kleinbuchstaben: {l}")

countCase("Das ist ein Text!")

def printTN(*namen):
	if len(namen) == 0:
		print("Keine Teilnehmer")
	elif len(namen) == 1:
		print(namen[0])
	else:
		gesamt = ""
		for tn in namen[0:-1]:
			gesamt += tn + ", "
		gesamt = gesamt.rstrip(", ")
		gesamt += " und " + namen[-1]
		print(gesamt)


n = [str(i) for i in range(4)]
# print(n[0:len(n)-1])
printTN(*n)