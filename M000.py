no1 = [x + 12 for x in range(1, 31) if x % 6 == 0]
print(no1)

text = "Ich bin ein Text"
no2 = [c.upper() for c in text if c.islower()]
print(no2)

no3 = [w[0].upper() for w in text.split(" ")]
print(no3)

no4 = [w for w in text.split(" ") if len(w) <= 3]
print(no4)