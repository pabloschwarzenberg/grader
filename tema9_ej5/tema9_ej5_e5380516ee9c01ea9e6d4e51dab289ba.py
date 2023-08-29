class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0] * 3 for _ in range(3)]

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
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == 1 else 3

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3

        return 1 if all(0 not in fila for fila in self.tablero) else 0


juego = JuegoDelGato()
juego.jugarGato(1, 1)
juego.jugarRaton()
print(juego.mostrar_tablero())
print(juego.indicarEstado())
