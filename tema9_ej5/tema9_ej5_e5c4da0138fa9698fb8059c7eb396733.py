import random

class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna]==0:
          self.tablero[fila][columna]=1
          return True
        return False

    def jugarRaton(self):
        fila =random.randint(0,2)
        columna = random.randint(0,2)
        if self.tablero[fila][columna]==0:
          return True
        return False

    def indicarEstado(self):
        t =self.tablero
        if t[0][0]==t[0][1]==t[0][2]==-1 or t[1][0]==t[1][1]==t[1][2] ==-1 or t[2][0]==t[2][1]==t[2][2] == -1 or \
        t[0][0]==t[1][0]==t[2][0] == -1 or t[0][1]==t[1][1]==t[2][1] == -1 or t[0][2]==t[1][2]==t[2][1] == -11 or \
        t[0][0]==t[1][1]==t[2][2] == -1 or t[0][2]==t[1][1]==t[2][0] == -1:
          return 3
        elif t[0][0]==t[0][1]==t[0][2]==1 or t[1][0]==t[1][1]==t[1][2] == 1 or t[2][0]==t[2][1]==t[2][2] == 1 or \
        t[0][0]==t[1][0]==t[2][0] == 1 or t[0][1]==t[1][1]==t[2][1] == 1 or t[0][2]==t[1][2]==t[2][1] == 1 or \
        t[0][0]==t[1][1]==t[2][2] == 1 or t[0][2]==t[1][1]==t[2][0] == 1:
          return 2
        elif 0 in t[0] or 0 in t[1] or 0 in t[2]:
          return 0
        else:
          return 1

    def cargar_tablero(self,tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         