class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_gato = 1  # Representa al gato
        self.jugador_raton = -1  # Representa al ratón
        self.turno = self.jugador_gato  # Comienza jugando el gato

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_gato
            self.turno = self.jugador_raton
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntaje = float('-inf')
        mejor_jugada = None

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = self.jugador_raton
                    puntaje = self.minimax(False)
                    self.tablero[i][j] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (i, j)

        if mejor_jugada is not None:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = self.jugador_raton
            self.turno = self.jugador_gato
            return True
        else:
            return False

    def minimax(self, es_maximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.obtenerPuntaje(estado)

        if es_maximizador:
            mejor_puntaje = float('-inf')

            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.jugador_raton
                        puntaje = self.minimax(False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)

            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')

            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.jugador_gato
                        puntaje = self.minimax(True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)

            return mejor_puntaje

    def obtenerPuntaje(self, estado):
        if estado == 1:
            return 0  # Empate
        elif estado == 2:
            return 1  # Gana el gato
        elif estado == 3:
            return -1  # Gana el ratón

    def indicarEstado(self):
        for i in range(3):
            # Filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == self.jugador_gato else 3

            # Columnas
            if self.tab
