from tkinter import Label
def berechne(op: str, a, b, output: Label):
	z1 = int(a)
	z2 = int(b)

	match op:
		case "Addition": output.config(text=f"{z1} + {z2} = {z1 + z2}")
		case "Subtraktion": output.config(text=f"{z1} - {z2} = {z1 - z2}")
		case "Multiplikation": output.config(text=f"{z1} * {z2} = {z1 * z2}")
		case "Division": output.config(text=f"{z1} / {z2} = {z1 / z2}")