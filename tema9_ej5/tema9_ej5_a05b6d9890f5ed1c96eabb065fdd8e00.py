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
        mejores_jugadas = []
        mejor_puntaje = float('-inf')

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejores_jugadas = [(fila, columna)]
                        mejor_puntaje = puntaje
                    elif puntaje == mejor_puntaje:
                        mejores_jugadas.append((fila, columna))

        if mejores_jugadas:
            fila, columna = random.choice(mejores_jugadas)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def minimax(self, depth, isMaximizing):
        estado = self.indicarEstado()

        if estado == 2:
            return 1
        elif estado == 3:
            return -1
        elif estado == 1:
            return 0

        if isMaximizing:
            mejor_puntaje = float('-inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntaje = self.minimax(depth + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)

            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntaje = self.minimax(depth + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)

            return mejor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobar filas
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2]:
                if self.tablero[fila][0] == 1:
                    return 2  # Ganó el gato
                elif self.tablero[fila][0] == -1:
                    return 3  # Ganó el ratón

        # Comprobar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna]:
                if self.tablero[0][columna] == 1:
                    return 2  # Ganó el gato
                elif self.tablero[0][columna] == -1:
                    return 3  # Ganó el ratón

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == 1:
                return 2  # Ganó el gato
            elif self.tablero[0][0] == -1:
                return 3  # Ganó el ratón

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]:
            if self.tablero[0][2] == 1:
                return 2  # Ganó el gato
            elif self.tablero[0][2] == -1:
                return 3  # Ganó el ratón

        # Comprobar empate
        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1  # Empate

        # No hay ganador y se puede seguir jugando
        return 0
