class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_actual = 1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_actual
            self.jugador_actual = -self.jugador_actual
            return True
        else:
            return False

    def jugarRaton(self):
        # Encuentra una posición vacía para la jugada del ratón
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.jugador_actual = -self.jugador_actual
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in self.tablero:
            if all(x == 1 for x in fila):
                return 2
            if all(x == -1 for x in fila):
                return 3

        for columna in range(3):
            if all(self.tablero[i][columna] == 1 for i in range(3)):
                return 2
            if all(self.tablero[i][columna] == -1 for i in range(3)):
                return 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 2
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3

        if all(all(x != 0 for x in fila) for fila in self.tablero):
            return 1

        return 0
