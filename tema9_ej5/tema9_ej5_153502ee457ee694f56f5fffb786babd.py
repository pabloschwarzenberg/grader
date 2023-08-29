class JuegoDelGato:
    def __init__(self):
        self.estado = 0
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        mostrar = ""
        tablero = self.mostrar_tablero()
        for i in range(len(tablero)):
            mostrar += str(tablero[i]) + "\n"
        return mostrar

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))

        if not movimientos:
            return False

        mejor_movimiento = None
        mejor_puntaje = -9999

        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = -1
            puntaje = self.minimax(False)
            self.tablero[fila][columna] = 0

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento

        if mejor_movimiento:
            fila, columna = mejor_movimiento
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def minimax(self, es_maximizador):
        resultado = self.indicarEstado()

        if resultado != 0:
            return self.obtener_puntaje(resultado)

        if es_maximizador:
            mejor_puntaje = -9999
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = 9999
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def obtener_puntaje(self, resultado):
        if resultado == 1:
            return 0
        elif resultado == 2:
            return 10
        elif resultado == 3:
            return -10

    def indicarEstado(self):
        # Verificar filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return self.tablero[i][0]

        # Verificar columnas
        for i in range(3

