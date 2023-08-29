class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_actual = 1

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    s += " "
                elif celda == 1:
                    s += "X"
                elif celda == -1:
                    s += "O"
                s += " "
            s += "\n"
        return s

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        return False

    def jugarRaton(self):
        mejor_puntaje = float("-inf")
        mejor_movimiento = None

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(self.tablero, 0, False)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_movimiento = (fila, columna)

        if mejor_movimiento:
            fila, columna = mejor_movimiento
            self.tablero[fila][columna] = -1
            self.jugador_actual = 1
            return True
        return False

    def minimax(self, tablero, profundidad, es_maximizador):
        estado = self.indicarEstado(tablero)

        if estado != 0:
            return estado

        if es_maximizador:
            mejor_puntaje = float("-inf")

            for fila in range(3):
                for columna in range(3):
                    if tablero[fila][columna] == 0:
                        tablero[fila][columna] = 1
                        puntaje = self.minimax(tablero, profundidad + 1, False)
                        tablero[fila][columna] = 0

                        mejor_puntaje = max(mejor_puntaje, puntaje)

            return mejor_puntaje

        else:
            mejor_puntaje = float("inf")

            for fila in range(3):
                for columna in range(3):
                    if tablero[fila][columna] == 0:
                        tablero[fila][columna] = -1
                        puntaje = self.minimax(tablero, profundidad + 1, True)
                        tablero[fila][columna] = 0

                        mejor_puntaje = min(mejor_puntaje, puntaje)

            return mejor_puntaje

    def indicarEstado(self, tablero=None):
        if not tablero:
            tablero = self.tablero

        for fila in range(3):
            if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] != 0:
                return 2 if tablero[fila][0] == 1 else