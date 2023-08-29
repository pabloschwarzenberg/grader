class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.jugador_actual = 1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_actual
            self.jugador_actual = -self.jugador_actual
            return True
        else:
            return False

    def jugarRaton(self):
        if self.indicarEstado() != 0:
            return False

        # Realizar la jugada más inteligente del ratón
        mejor_puntaje = float('-inf')
        mejor_fila = -1
        mejor_columna = -1

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_fila = fila
                        mejor_columna = columna

        if mejor_fila != -1 and mejor_columna != -1:
            self.tablero[mejor_fila][mejor_columna] = -1
            self.jugador_actual = 1
            return True
        else:
            return False

    def minimax(self, profundidad, es_maximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.asignarPuntaje(estado, profundidad)

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

    def asignarPuntaje(self, estado, profundidad):
        if estado == 1: