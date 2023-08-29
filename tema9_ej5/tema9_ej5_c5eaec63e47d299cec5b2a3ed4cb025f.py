class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero vacío
        self.turno_gato = True  # Indica el turno del gato, True para el gato, False para el ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            if self.turno_gato:
                self.tablero[fila][columna] = 1
            else:
                self.tablero[fila][columna] = -1
            self.turno_gato = not self.turno_gato
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntaje = float('-inf')
        mejor_movimiento = None

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    puntaje = self.minimax(False)
                    self.tablero[i][j] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_movimiento = (i, j)

        if mejor_movimiento is not None:
            self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = -1
            self.turno_gato = not self.turno_gato
            return True
        else:
            return False

    def minimax(self, es_maximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return estado

        if es_maximizador:
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
        # Verificar si hay ganador en filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

        # Verificar si hay ganador en columnas
        for i in range(3):
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
               

         