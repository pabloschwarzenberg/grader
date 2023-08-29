import random
from tkinter import *
from tkinter import messagebox
from matriz import *
import sys

principal = Tk()
principal.title("Gato")
botones=[]
turno=0
gato=PhotoImage(file="gato.png")
raton=PhotoImage(file="raton.png")
vacio=PhotoImage(file="vacio.png")
tablero=Matriz([[0,0,0],[0,0,0],[0,0,0]])

def revisar_ganador(x,y,turno):
    fila=tablero.getFila(x)
    cuenta1=fila.count(turno)
    columna=tablero.getColumna(y)
    cuenta2=columna.count(turno)
    if cuenta1==3 or cuenta2==3:
        messagebox.showinfo("Juego del Gato", "Tenemos un Ganador")
        sys.exit(0)
    if x==y:
        diagonal=tablero.getDiagonalIzquierda()
        if diagonal.count(turno)==3:
            messagebox.showinfo("Juego del Gato", "Tenemos un Ganador")
            sys.exit(0)
    if x==2-y:
        diagonal=tablero.getDiagonalDerecha()
        if diagonal.count(turno)==3:
            messagebox.showinfo("Juego del Gato", "Tenemos un Ganador")
            sys.exit(0)

def click(evento):
    global turno
    global tablero
    if evento.widget["text"]=="":
        if turno==0:
            jugada=1
            evento.widget["image"]=gato
            tablero.set(evento.widget.x,evento.widget.y,jugada)
            turno=1
        else:
            jugada=-1
            evento.widget["image"]=raton
            tablero.set(evento.widget.x,evento.widget.y,jugada)
            turno=0
        revisar_ganador(evento.widget.x,evento.widget.y,jugada)

for i in range(3):
    fila=[]
    for j in range(3):
        b1=Button(principal,image=vacio,width="80",height="80")
        b1.bind("<Button-1>",click)
        b1.x=i
        b1.y=j
        b1.grid(row=i,column=j)
        fila.append(b1)
    botones.append(fila)

mainloop()