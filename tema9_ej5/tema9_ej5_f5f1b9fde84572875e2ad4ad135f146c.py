class JuegoDelGato:
    def init(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def repr(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        if self.indicarEstado() != 0:
            return False

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != 0:
                return 2 if self.tablero[0][j] == 1 else 3

        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or (
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3

        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        return 0

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero