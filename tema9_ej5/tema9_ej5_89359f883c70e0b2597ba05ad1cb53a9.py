class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.turno_gato = True

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntuacion = float('-inf')
        mejor_fila = -1
        mejor_columna = -1

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntuacion = self._minimax(0, False)
                    self.tablero[fila][columna] = 0

                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        mejor_fila = fila
                        mejor_columna = columna

        if mejor_fila != -1 and mejor_columna != -1:
            self.tablero[mejor_fila][mejor_columna] = -1
            self.turno_gato = True
            return True
        else:
            return False

    def _minimax(self, profundidad, es_maximizador):
        estado = self.indicarEstado()
        if estado != 0:
            return estado

        if es_maximizador:
            mejor_puntuacion = float('-inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntuacion = self._minimax(profundidad + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)
            return mejor_puntuacion
        else:
            mejor_puntuacion = float('inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntuacion = self._minimax(profundidad + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)
            return mejor_puntuacion

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and len(matriz[0]) == 3:
            self.tablero = matriz

    def indicarEstado(self):
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            if fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Ganó el gato
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ganó el ratón

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 2  # Ganó el gato
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 3  # Ganó el ratón

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón

        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        return 0  # No hay ganador, se puede seguir jugando

         