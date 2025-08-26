for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0:
		print("FizzBuzz")
	elif x % 3 == 0:
		print("Fizz")
	elif x % 5 == 0:
		print("Buzz")
	else:
		print(x)

for x in range(1, 201):
	if x % 100 in [11, 12, 13]:
		print(f"{x}th")
	elif x % 10 == 1:
		print(f"{x}st")
	elif x % 10 == 2:
		print(f"{x}nd")
	elif x % 10 == 3:
		print(f"{x}rd")
	else:
		print(f"{x}th")

# import time
for x in range(0, 60):
	for y in range(0, 60):
		print(f"{x:02}:{y:02}")
		# time.sleep(1)

for x in range(0, 3600):
	print(f"{int(x/60):02}:{(x % 60):02}")

for x in range(1, 11):
	for y in range(1, 11):
		print(f"{x} x {y} = {x * y}")