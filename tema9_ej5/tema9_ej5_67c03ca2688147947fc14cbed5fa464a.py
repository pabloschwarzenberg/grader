class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.jugador_actual = 1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntaje = float('-inf')
        mejor_jugada = None

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[i][j] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (i, j)

        if mejor_jugada is not None:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1
            self.jugador_actual = 1
            return True
        else:
            return False

    def minimax(self, profundidad, es_maximizando):
        resultado = self.indicarEstado()

        if resultado != 0:
            return resultado

        if es_maximizando:
            mejor_puntaje = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = -1
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3

        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or \
           (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3

        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        return 0