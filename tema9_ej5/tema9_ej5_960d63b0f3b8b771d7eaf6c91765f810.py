class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno_gato = True

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
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
                        mejor_puntaje = puntaje
                        mejores_jugadas = [(fila, columna)]
                    elif puntaje == mejor_puntaje:
                        mejores_jugadas.append((fila, columna))

        if len(mejores_jugadas) > 0:
            fila, columna = random.choice(mejores_jugadas)
            self.tablero[fila][columna] = -1
            self.turno_gato = True
            return True
        else:
            return False

    def minimax(self, profundidad, es_maximizador):
        estado = self.indicarEstado()

        if estado == 2:
            return 1
        elif estado == 3:
            return -1
        elif estado == 1:
            return 0

        if es_maximizador:
            mejor_puntaje = float('-inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)

            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)

            return mejor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in range(3):
            # Comprobar filas
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == 1 else 3

            # Comprobar columnas
            if self.tablero[0][fila] == self.tablero[1][fila] == self.tablero[2][fila] != 0:
                return 2 if self.tablero[0][fila] == 1 else 3

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Comprobar empate
        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1

        # No hay ganador, se puede seguir jugando
        return 0
