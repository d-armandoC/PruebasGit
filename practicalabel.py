from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
milabel= Label(miFrame, text="Hola alumnos Python")
milabel.place(x=100, y=200)
miImagen=PhotoImage(file="imagen.png")
milabel2=Label(miFrame, image=miImagen)
milabel2.place(x=100, y=5)

cuadro1=Entry(miFrame)
cuadro1.place(x=100, y=250)
cuadro1.config(bg="red",bd=5, fg="white", justify="center")

cuadro2=Entry(miFrame)
cuadro2.place(x=100, y=300)
cuadro2.config(bg="red",bd=5, fg="white", justify="center")

cuadro3=Entry(miFrame)
cuadro3.place(x=100, y=350)
cuadro3.config(bg="red",bd=5, fg="white", justify="center")

root.mainloop()