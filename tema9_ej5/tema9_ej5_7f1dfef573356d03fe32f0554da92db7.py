class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0,0,0],[0,0,0],[0,0,0]]
        
    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        h = []
        d = [-1,1]
        for j in d:
            for i in range(3):
                if self.tablero[i] == [j,j,0] or self.tablero[i] == [0,j,j] or self.tablero[i] == [j,0,j]:
                    self.tablero[i][self.tablero[i].index(0)] = -1
                    return True
            for i in range(3):
                for k in range(3):
                    h.append(self.tablero[k][i])
                if h == [j,j,0] or h == [0,j,j] or h == [j,0,j]:
                    self.tablero[h.index(0)][i] = -1
                    return True
        return False

    def indicarEstado(self):
        h = []
        d = [-1,1]
        c = 0
        for j in d:
            for i in range(3):
                if self.tablero[i] == [j,j,j]:
                    c += 1
            for i in range(3):
                for k in range(3):
                    h.append(self.tablero[k][i])
                if h == [j,j,j]:
                    c += 1
            for i in range(3):
                h1 = [self.tablero[0][0],self.tablero[1][1],self.tablero[2][2]]
                h2 = [self.tablero[0][2],self.tablero[1][1],self.tablero[2][0]]
                if h1 == [j,j,j]:
                    c+=1
                if h2 == [j,j,j]:
                    c+=1

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
         