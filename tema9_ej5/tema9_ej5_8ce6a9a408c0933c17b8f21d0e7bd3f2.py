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

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    puntaje = self.minimax(False)
                    self.tablero[i][j] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (i, j)

        if mejor_jugada:
            self.tablero[mejor_jugada[0]][mejor_jugada[1]] = -1
            return True
        else:
            return False

    def minimax(self, esTurnoGato):
        estado = self.indicarEstado()

        if estado == 1:
            return 0
        elif estado == 2:
            return 1
        elif estado == 3:
            return -1

        if esTurnoGato:
            mejor_puntaje = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobación de empate
        empate = True
        for fila in self.tablero:
            if 0 in fila:
                empate = False
                break
        if empate:
            return 1

        # Comprobación de filas y columnas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                if self.tablero[i][0] == 1:
                    return 2
                else:
                    return 3
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                if self.tablero[0][i] == 1:
                    return 2
                else:
                    return 3

        # Comprobación de diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                return 2
            else:
                return 3
        if self.tablero[2][0] == self.tablero[1][1] == self.tablero[0][2] != 0:
            if self.tablero[2][0] == 1:
                return 2
            else:
                return 3

        # No hay ganador y se puede seguir jugando
        return 0

         