class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        mejores_movimientos = []
        mejor_puntuacion = float('-inf')

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntuacion = self.minimax(False)
                    self.tablero[fila][columna] = 0

                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        mejores_movimientos = [(fila, columna)]
                    elif puntuacion == mejor_puntuacion:
                        mejores_movimientos.append((fila, columna))

        if mejores_movimientos:
            fila, columna = mejores_movimientos[0]
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def minimax(self, esMaximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.puntuacion(estado)

        if esMaximizador:
            mejor_puntuacion = float('-inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntuacion = self.minimax(False)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)
            return mejor_puntuacion
        else:
            mejor_puntuacion = float('inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntuacion = self.minimax(True)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)
            return mejor_puntuacion

    def puntuacion(self, estado):
        if estado == 1:
            return 0
        elif estado == 2:
            return 1
        elif estado == 3:
            return -1

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                if self.tablero[fila][0] == 1:
                    return 2  # Gana el gato
                else:
                    return 3  # Gana el ratón

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == 1:
                    return 2  # Gana el gato
                else:
                    return 3  # Gana el ratón

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                return 2  # Gana el gato
            else:
                return 3  # Gana el ratón

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == 1:
                return 2  # Gana el gato
            else:
                return 3  # Gana el ratón

        if self.tablero_lleno():
            return 1  # Empate

        return 0  # Juego en curso

    def tablero_lleno(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return False
        return True
