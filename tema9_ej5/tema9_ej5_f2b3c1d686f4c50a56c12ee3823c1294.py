class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]
    def __repr__(self):
        representation = ""
        for fila in self.tablero:
            representation += " ".join(map(str, fila)) + "\n"
        return representation
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero
    def cargar_tablero(self, matriz):
        self.tablero = matriz
    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2]:
                if self.tablero[fila][0] == 1:
                    return 2 
                elif self.tablero[fila][0] == -1:
                    return 3 

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna]:
                if self.tablero[0][columna] == 1:
                    return 2 
                elif self.tablero[0][columna] == -1:
                    return 3 

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == 1:
                return 2 
            elif self.tablero[0][0] == -1:
                return 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]:
            if self.tablero[0][2] == 1:
                return 2 
            elif self.tablero[0][2] == -1:
                return 3

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return 0 
        return 1 

if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)