class JuegoDelGato:

    def __init__(self):
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        pass

    def jugarRaton(self):
        pass

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        pass

    def mostrar_tablero(self):
        return [[-1,-1,0],[0,1,0],[1,1,0]]

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  
        self.jugador_actual = 1  
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:  
            self.tablero[fila][columna] = 1  
            self.jugador_actual = -1  
            return True
        else:
            return False
    def jugarRaton(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:  
                    self.tablero[fila][columna] = -1  
                    self.jugador_actual = 1  
                    return True
        return False
    def mostrar_tablero(self):
        return self.tablero
    def cargar_tablero(self, matriz):
        self.tablero = matriz
    def indicarEstado(self):
        for jugador in [1, -1]:
            for fila in range(3):
                if self.tablero[fila] == [jugador] * 3:
                    return 2 if jugador == 1 else 3
            for columna in range(3):
                if [self.tablero[fila][columna] for fila in range(3)] == [jugador] * 3:
                    return 2 if jugador == 1 else 3
            if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:
                return 2 if jugador == 1 else 3
            if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:
                return 2 if jugador == 1 else 3
        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1
        return 0         