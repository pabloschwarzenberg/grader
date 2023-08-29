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
        mejor_jugada = None
        mejor_puntaje = float('-inf')

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (fila, columna)

        if mejor_jugada:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def minimax(self, depth, is_maximizing):
        estado = self.indicarEstado()

        if estado == 2:
            return 1
        elif estado == 3:
            return -1
        elif estado == 1:
            return 0

        if is_maximizing:
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
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                if self.tablero[fila][0] == 1:
                    return 2  # Gato gana
                else:
                    return 3  # Ratón gana

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == 1:
                    return 2  # Gato gana
                else:
                    return 3 
