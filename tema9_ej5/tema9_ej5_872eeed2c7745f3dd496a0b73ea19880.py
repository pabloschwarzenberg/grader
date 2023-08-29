class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def cargar(self,archivo):
        archivo=open(archivo,"r")
        self.celdas=[]
        for linea in archivo:
            linea=linea.strip().split(",")
            linea=list(map(int,linea))
            self.celdas.append(linea)
        archivo.close()

    def grabar(self,archivo):
        archivo=open(archivo,"w")
        for fila in self.celdas:
            fila=list(map(str,fila))
            s=",".join(fila)
            s=s+"\n"
            archivo.write(s)
        archivo.close()

    def __add__(self,other):
        r=[]
        if(len(self.celdas)!=len(other.celdas)):
            return None
        for i in range(len(self.celdas)):
            fila=[]
            for j in range(len(self.celdas)):
                c=self.celdas[i][j]+other.celdas[i][j]
                fila.append(c)
            r.append(fila)
        resultado=Matriz(r)
        return resultado

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def getFila(self,i):
        return self.celdas[i]

    def getColumna(self,i):
        r=[]
        for j in range(len(self.celdas)):
            r.append(self.celdas[j][i])
        return r

    def getDiagonalIzquierda(self):
        r=[]
        for i in range(len(self.celdas)):
            r.append(self.celdas[i][i])
        return r

    def getDiagonalDerecha(self):
        r=[]
        for i in range(len(self.celdas)):
            r.append(self.celdas[i][len(self.celdas)-i-1])
        return r

    def set(self,i,j,valor):
        self.celdas[i][j]=valor

import random
from tkinter import *
from tkinter import messagebox
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



if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         