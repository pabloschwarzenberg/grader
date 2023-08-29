import random
from tkinter import *
from tkinter import messagebox
from matriz import *
import sys
import math

principal = Tk()
principal.title("Gato")

botones=[]
turno=1
primera_jugada=True
gato=PhotoImage(file="gato.png")
raton=PhotoImage(file="raton.png")
vacio=PhotoImage(file="vacio.png")
tablero=Matriz([[0,0,0],[0,0,0],[0,0,0]])

def buscarPosiblesJugadas():
    return tablero.getCeldasVacias()

def evaluarTablero():
    r=[[0,0,0],[0,0,0],[0,0,0]]
    ganador=0
    vacias=0
    for i in range(len(tablero.celdas)):
        suma_fila=0
        suma_columna=0
        for j in range(len(tablero.celdas)):
            suma_fila=suma_fila+tablero.celdas[i][j]
            suma_columna=suma_columna+tablero.celdas[j][i]
            if tablero.celdas[i][j]==0:
                vacias=vacias+1
        r[0][i]=suma_fila
        if(math.fabs(suma_fila)==3):
            ganador=suma_fila//3
        r[1][i]=suma_columna
        if(math.fabs(suma_columna)==3):
            ganador=suma_columna//3
    suma_diagonal1=0
    suma_diagonal2=0
    for i in range(len(tablero.celdas)):
        suma_diagonal1=suma_diagonal1+tablero.celdas[i][i]
        suma_diagonal2=suma_diagonal2+tablero.celdas[i][2-i]
    r[2][0]=suma_diagonal1
    if(math.fabs(suma_diagonal1)==3):
        ganador=suma_diagonal1//3
    r[2][1]=suma_diagonal2
    if(math.fabs(suma_diagonal2)==3):
        ganador=suma_diagonal2//3
    if ganador!=0:
        r[2][2]=ganador
    if vacias==0:
        r[2][2]=-2
    return r

def evaluarJugadaParaCondicion(estado,condicion):
    for i in range(3):
        if estado[0][i]==condicion:
            p=tablero.getCeldaVaciaFila(i)
            if(len(p)!=0):
                return p[0]
        if estado[1][i]==condicion:
            p=tablero.getCeldaVaciaColumna(i)
            if(len(p)!=0):
                return p[0]
    if estado[2][0]==condicion:
        p=tablero.getCeldaVaciaDiagonalIzquierda()
        if(len(p)!=0):
            return p[0]
    if estado[2][1]==condicion:
        p=tablero.getCeldaVaciaDiagonalDerecha()
        if(len(p)!=0):
            return p[0]
    #la condicion no existe en el tablero
    return None

def escogerJugada(estado,turno):
    if estado[2][2]!=0:
        return None

    #Jugadas para ganar
    condicion=turno*2
    p=evaluarJugadaParaCondicion(estado,condicion)
    if not (p is None):
        return p

    #Jugadas para evitar que me ganen
    condicion=turno*-2
    p=evaluarJugadaParaCondicion(estado,condicion)
    if not (p is None):
        return p

    #Jugadas para tratar de ganar
    condicion=turno
    p=evaluarJugadaParaCondicion(estado,condicion)
    if not (p is None):
        return p

    #Jugadas para interferir con el oponente
    condicion=turno*-1
    p=evaluarJugadaParaCondicion(estado,condicion)
    if not (p is None):
        return p

    #juego en cualquier celda vacia
    p=tablero.getCeldasVacias()
    if len(p)!=0:
        return p[0]

def escogerPrimeraJugadaGato():
    if tablero.celdas[1][1]==0:
        return [1,1]
    else:
        return [0,2]

def click(evento):
    global turno
    global tablero
    global primera_jugada
    if evento.widget["text"]=="":
        if turno==1:
            evento.widget["image"]=raton
            tablero.set(evento.widget.x,evento.widget.y,turno)

            estado=evaluarTablero()
            if estado[2][2]==1:
                messagebox.showinfo("Juego del Gato","Gano el Raton")
                sys.exit(0)

            turno=-1

            if primera_jugada:
                p=escogerPrimeraJugadaGato()
                primera_jugada=False
            else:
                p=escogerJugada(estado,turno)
                if estado[2][2]==-2 or p is None:
                    messagebox.showinfo("Juego del Gato","Ya no se puede seguir jugando")
                    sys.exit(0)

            botones[p[0]][p[1]]["image"]=gato
            tablero.set(p[0],p[1],turno)

            estado=evaluarTablero()
            if estado[2][2]==-1:
                messagebox.showinfo("Juego del Gato","Gano el Gato")
                sys.exit(0)
            if estado[2][2]==-2:
                messagebox.showinfo("Juego del Gato","Ya no se puede seguir jugando")
                sys.exit(0)
            turno=1

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
