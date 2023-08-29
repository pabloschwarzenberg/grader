class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.jugador_actual = 1  # 1 para el gato, -1 para el ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        else:
            return False

    def jugarRaton(self):
        mejores_jugadas = []
        mejor_puntuacion = float('-inf')
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    puntuacion = self.minimax(self.tablero, False)
                    self.tablero[i][j] = 0
                    if puntuacion > mejor_puntuacion:
                        mejores_jugadas = [(i, j)]
                        mejor_puntuacion = puntuacion
                    elif puntuacion == mejor_puntuacion:
                        mejores_jugadas.append((i, j))
        if mejores_jugadas:
            fila, columna = mejores_jugadas[0]
            self.tablero[fila][columna] = -1
            self.jugador_actual = 1
            return True
        else:
            return False

    def minimax(self, tablero, es_maximizador):
        estado = self.indicarEstado(tablero)
        if estado != 0:
            return estado
        if es_maximizador:
            mejor_puntuacion = float('-inf')
            for i in range(3):
                for j in range(3):
                    if tablero[i][j] == 0:
                        tablero[i][j] = 1
                        puntuacion = self.minimax(tablero, False)
                        tablero[i][j] = 0
                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)
            return mejor_puntuacion
        else:
            mejor_puntuacion = float('inf')
            for i in range(3):
                for j in range(3):
                    if tablero[i][j] == 0:
                        tablero[i][j] = -1
                        puntuacion = self.minimax(tablero, True)
                        tablero[i][j] = 0
                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)
            return mejor_puntuacion

    def mostrar_tablero(self):
        return [[self.tablero[i][j] for j in range(3)] for i in range(3)]

    def cargar_tablero(self, matriz):
        self.tablero = [[matriz[i][j] for j in range(3)] for i in range(3)]

    def indicarEstado(self):
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
        # Empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1
        # No hay ganador, se puede seguir jugando
        return 0