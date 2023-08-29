class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        if self.indicarEstado() != 0:
            return False

        # Lógica para la jugada del ratón
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True

        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for fila in self.tablero:
            if all(cell == 1 for cell in fila):
                return 2  # Gato ganador
            if all(cell == -1 for cell in fila):
                return 3  # Ratón ganador

        # Verificar columnas
        for columna in range(3):
            if all(self.tablero[fila][columna] == 1 for fila in range(3)):
                return 2
            if all(self.tablero[fila][columna] == -1 for fila in range(3)):
                return 3

        # Verificar diagonales
        if all(self.tablero[i][i] == 1 for i in range(3)) or all(self.tablero[i][2 - i] == 1 for i in range(3)):
            return 2
        if all(self.tablero[i][i] == -1 for i in range(3)) or all(self.tablero[i][2 - i] == -1 for i in range(3)):
            return 3

        # Verificar empate
        if all(cell != 0 for fila in self.tablero for cell in fila):
            return 1  # Empate

        return 0  # Juego en curso
