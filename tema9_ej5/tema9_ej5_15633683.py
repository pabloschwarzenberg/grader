import random
class JuegoDelGato:

    def __init__(self,tablero=[]):
        self.tablero=[[0,0,0],[0,0,0],[0,0,0]]
        pass

    def __repr__(self):
        return '{0}'.format(self.tablero)

    def jugarGato(self,fila,columna):
        self.fila=fila
        self.columna=columna
        if self.tablero[fila][columna]==0:
            self.tablero[fila][columna]=1
            return True
        else:
            return False
        pass

    def jugarRaton(self):
        if self.tablero[0][0]==self.tablero[0][1]==-1:
            self.tablero[0][2]=-1
            return True
        fila_raton=random.randint(0,2)
        columna_raton=random.randint(0,2)
        if self.tablero[fila_raton][columna_raton]==0:
            self.tablero[fila_raton][columna_raton]=-1
            return True
        else:
            return False
        pass

    def indicarEstado(self):
        if self.tablero[0][0]==self.tablero[0][1]==self.tablero[0][2]==1 or self.tablero[1][0]==self.tablero[1][1]==self.tablero[1][2]==1 or self.tablero[2][0]==self.tablero[2][1]==self.tablero[2][2]==1 or self.tablero[0][0]==self.tablero[1][0]==self.tablero[2][0]==1 or self.tablero[0][1]==self.tablero[1][1]==self.tablero[2][1]==1 or self.tablero[0][2]==self.tablero[1][2]==self.tablero[2][2]==1 or self.tablero[0][0]==self.tablero[1][1]==self.tablero[2][2]==1 or self.tablero[0][2]==self.tablero[1][1]==self.tablero[2][0]==1:
            return 2
        elif self.tablero[0][0]==self.tablero[0][1]==self.tablero[0][2]==-1 or self.tablero[1][0]==self.tablero[1][1]==self.tablero[1][2]==-1 or self.tablero[2][0]==self.tablero[2][1]==self.tablero[2][2]==-1 or self.tablero[0][0]==self.tablero[1][0]==self.tablero[2][0]==-1 or self.tablero[0][1]==self.tablero[1][1]==self.tablero[2][1]==-1 or self.tablero[0][2]==self.tablero[1][2]==self.tablero[2][2]==-1 or self.tablero[0][0]==self.tablero[1][1]==self.tablero[2][2]==-1 or self.tablero[0][2]==self.tablero[1][1]==self.tablero[2][0]==-1:
            return 3
        pass

    def cargar_tablero(self,tablero):
        self.tablero=tablero
        pass

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