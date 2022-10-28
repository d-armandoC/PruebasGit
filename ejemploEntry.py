from cgitb import text
from tkinter import *


root=Tk()
miNombre =StringVar()
root.geometry("600x350")
miFrame=Frame(root, width=1200, height=600)
miFrame.pack()
#labels
labelNombre=Label(miFrame, text="Nombre:")
labelNombre.grid(row=0, column=0, pady=5)
nombre=Entry(miFrame, text=miNombre)
#nombre.config(bg="red",bd=5, fg="white", justify="center")
nombre.grid(row=0, column=1, pady=5)

labelApellido=Label(miFrame, text="Apellido:")
labelApellido.grid(row=1, column=0, pady=5)
apellido=Entry(miFrame)
apellido.grid(row=1, column=1, pady=5)

labeldireccion=Label(miFrame, text="Direccion:")
labeldireccion.grid(row=3, column=0, pady=5)
direccion=Entry(miFrame)
direccion.grid(row=3, column=1, pady=5)


labelPass=Label(miFrame, text="Password:")
labelPass.grid(row=4, column=0, pady=5)
passw=Entry(miFrame, show="*")
passw.grid(row=4, column=1, pady=5)

labelComent=Label(miFrame, text="Comentario:")
labelComent.grid(row=5, column=0, pady=5)
coment=Text(miFrame, width=13, height=5)
coment.grid(row=5, column=1, pady=5)
def codigoBoton():
    miNombre.set("Diego")
    print(miNombre.get())

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()