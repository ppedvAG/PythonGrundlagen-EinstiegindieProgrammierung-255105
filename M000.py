list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5, 6]
list3 = [5, 6, 7, 8]

# if len(list1) > len(list2) and len(list1) > len(list3):
# 	print("list1 ist die längste Liste")

laengen = [len(list1), len(list2), len(list3)]

laengen.sort()

laengste = laengen[-1]  # Höchste Länge am Ende

if len(list1) == laengste:
	print("list1 ist die längste")
if len(list2) == laengste:
	print("list2 ist die längste")
if len(list3) == laengste:
	print("list3 ist die längste")


list4 = list1 + list2 + list3
if 3 in list4 or 7 in list4 or 10 in list4:
	print("...")

intersection = {3, 7, 10}.intersection(list4)
if len(intersection) > 0:
	print(intersection)