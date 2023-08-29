class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntuacion = float('-inf')
        mejor_movimiento = None

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    puntuacion = self.minimax(False)
                    self.tablero[fila][columna] = 0

                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        mejor_movimiento = (fila, columna)

        if mejor_movimiento:
            fila, columna = mejor_movimiento
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def minimax(self, esMaximizador):
        resultado = self.indicarEstado()

        if resultado != 0:
            return resultado

        if esMaximizador:
            mejor_puntuacion = float('-inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = self.gato
                        puntuacion = self.minimax(False)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)

            return mejor_puntuacion
        else:
            mejor_puntuacion = float('inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = self.raton
                        puntuacion = self.minimax(True)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)

            return mejor_puntuacion

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == self.gato else 3

        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == self.gato else 3

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == self.gato else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == self.gato else 3

        # Verificar empate
        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1

        # El juego no ha terminado
        return 0