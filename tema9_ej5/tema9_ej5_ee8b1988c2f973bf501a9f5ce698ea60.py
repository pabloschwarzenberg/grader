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
        mejor_jugada = self.buscarMejorJugada(-1)
        if mejor_jugada:
            self.tablero[mejor_jugada[0]][mejor_jugada[1]] = -1
            return True
        else:
            return False

    def buscarMejorJugada(self, jugador):
        mejor_puntaje = float('-inf')
        mejor_jugada = None

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = jugador
                    puntaje = self.minimax(0, False)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (fila, columna)

        return mejor_jugada

    def minimax(self, profundidad, esMaximizando):
        resultado = self.indicarEstado()

        if resultado != 0:
            return resultado

        if esMaximizando:
            mejor_puntaje = float('-inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = max(puntaje, mejor_puntaje)

            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = min(puntaje, mejor_puntaje)

            return mejor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz
        else:
            raise ValueError("La matriz debe ser de 3x3.")

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

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón

        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        return 0  # Juego en curso
