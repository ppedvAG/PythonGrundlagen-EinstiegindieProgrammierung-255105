# GUI
# Es gibt verschiedene Python GUI Frameworks
# tkinter (in der Standardbibliothek), pyQT, pyGUI, pySimpleGui, Kivy (u.a. mobile Entwicklung)

# Grundaufbau
from tkinter import *  # Schritt 1
from tkinter import messagebox
from M013b import *

window = Tk()  # Schritt 2

# Ab hier wird die GUI gebaut
window.wm_title("Mein erstes Fenster")
window.geometry("500x500+2500+300")
window.config(bg="Green")  # config: Konfiguration von Widgets (GUI-Komponenten)

###############

l1 = Label(text="Zahl 1")
l1.place(width=50, height=20, x=20, y=20)

e1 = Entry()
e1.place(width=150, height=20, x=80, y=20)

###############

l2 = Label(text="Zahl 2")
l2.place(width=50, height=20, x=20, y=50)

e2 = Entry()
e2.place(width=150, height=20, x=80, y=50)

###############

def writeValue(s: StringVar):
	global selected
	selected = s
op = OptionMenu(window, StringVar(value="Rechenoperation"),
				"Addition", "Subtraktion", "Multiplikation", "Division",
				command=lambda s: writeValue(s))
op.place(width=210, height=30, x=20, y=80)

outputL = Label()
outputL.place(width=150, height=30, x=50, y=160)

btn = Button(text="Berechnen")
btn.place(width=150, height=30, x=50, y=120)  # place: Legt die Komponente in das Fenster hinein
btn.config(command=lambda: berechne(selected, e1.get(), e2.get(), outputL))

for i in range(10):
	l = Label(text=i, name=f"label{i}")
	l.place(width=100, height=30, x=20, y=200+(i*35))
window.nametowidget("label5").config(text="Hallo")  # nametowidget: Komponente über einen Namen angreifen

# messagebox.askyesno(title="Hallo", message="Eine Nachricht")

window.mainloop()  # Schritt 3