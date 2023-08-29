class JuegoDelGato:
    def _init_(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def _repr_(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Buscar la jugada más inteligente del ratón (estrategia ficticia)
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def indicarEstado(self):
        # Verificar si hay un ganador
        for i in range(3):
            # Filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3
            # Columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3
        # Diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Verificar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        # Si no hay ganador ni empate, se puede seguir jugando
        return 0

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero