z1 = 3
z2 = 5
z3 = 8
summe = z1 + z2 + z3
print(summe)

potenz = summe ** summe
print(potenz)

print(potenz % 2)

v = "Max"
n = "Mustermann"
vn = v + n
print(vn.lower().count("m"))
print(vn.count("m") + vn.count("M"))

vorname = "lukas"
print(vorname.title())
print(vorname.capitalize())
print(vorname[0].upper() + vorname[1:].lower())

print(len(v + n + vorname))