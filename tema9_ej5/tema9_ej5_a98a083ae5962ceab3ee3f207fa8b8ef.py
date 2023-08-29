class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return ""

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            return True
        else:
            return False

    def jugarRaton(self):
        for x in range(len(self.tablero)):
            for y in range(len(self.tablero[x])):
                if self.tablero[x][y]==0:
                    self.tablero[x][y]=-1
                    if self.ganarraton()==True:
                        return True
                    else:
                        self.tablero[x][y]=0

    def ganargato(self):
        if self.tablero[0][0]==1 and self.tablero[0][1]==1 and self.tablero[0][2]==1:
            return True
        elif self.tablero[1][0]==1 and self.tablero[1][1]==1 and self.tablero[1][2]==1:
            return True
        elif self.tablero[2][0] == 1 and self.tablero[2][1] == 1 and self.tablero[2][2] == 1:
            return True


        elif self.tablero[0][0] == 1 and self.tablero[1][0] == 1 and self.tablero[2][0] == 1:
            return True
        elif self.tablero[0][1] == 1 and self.tablero[1][1] == 1 and self.tablero[2][1] == 1:
            return True
        elif self.tablero[0][2] == 1 and self.tablero[1][2] == 1 and self.tablero[2][2] == 1:
            return True

        elif self.tablero[0][0] == 1 and self.tablero[1][1] == 1 and self.tablero[2][2] == 1:
            return True
        elif self.tablero[2][0] == 1 and self.tablero[1][1] == 1 and self.tablero[0][2] == 1:
            return True
    def ganarraton(self):
        if self.tablero[0][0]==-1 and self.tablero[0][1]==-1 and self.tablero[0][2]==-1:
            return True
        elif self.tablero[1][0]==-1 and self.tablero[1][1]==-1 and self.tablero[1][2]==-1:
            return True
        elif self.tablero[2][0] == -1 and self.tablero[2][1] == -1 and self.tablero[2][2] == -1:
            return True


        elif self.tablero[0][0] == -1 and self.tablero[1][0] == -1 and self.tablero[2][0] == 1:
            return True
        elif self.tablero[0][1] == -1 and self.tablero[1][1] == -1 and self.tablero[2][1] == -1:
            return True
        elif self.tablero[0][2] == -1 and self.tablero[1][2] == -1 and self.tablero[2][2] == -1:
            return True

        elif self.tablero[0][0] == -1 and self.tablero[1][1] == -1 and self.tablero[2][2] == -1:
            return True
        elif self.tablero[2][0] == -1 and self.tablero[1][1] == -1 and self.tablero[0][2] == -1:
            return True




    def indicarEstado(self):
        for cada in self.tablero:
            for columna in cada:
                if columna==0:
                    return 0
        if self.ganargato()==True:
            return 2
        elif self.ganarraton()==True:
            return 3
        else:
            return 1

    def cargar_tablero(self, tablero):
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
         