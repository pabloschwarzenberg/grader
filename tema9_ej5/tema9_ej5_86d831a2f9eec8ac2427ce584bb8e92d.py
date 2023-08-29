class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Encuentra la mejor jugada para el ratón.
        mejor_jugada = None
        mejor_puntaje = -2

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    puntaje = self.minimax(1)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejor_jugada = (fila, columna)
                        mejor_puntaje = puntaje

        # Juega la mejor jugada.
        if mejor_jugada is not None:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def minimax(self, profundidad):
        estado = self.indicarEstado()

        if estado != 0:
            return estado * profundidad

        if profundidad % 2 == 0:
            jugador = self.gato
            mejor_puntaje = -2

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = jugador
                        puntaje = self.minimax(profundidad + 1)
                        self.tablero[fila][columna] = 0

                        if puntaje > mejor_puntaje:
                            mejor_puntaje = puntaje

            return mejor_puntaje
        else:
            jugador = self.raton
            peor_puntaje = 2

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = jugador
                        puntaje = self.minimax(profundidad + 1)
                        self.tablero[fila][columna] = 0

                        if puntaje < peor_puntaje:
                            peor_puntaje = puntaje

            return peor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verifica si hay un ganador.
        for jugador in [self.gato, self.raton]:
            for fila in range(3):
                if sum(self.tablero[fila]) == jugador * 3:
                    return jugador

            for columna in range(3):
                if sum([self.tablero[i][columna] for i in range(3)]) == jugador * 3:
                    return jugador

            if sum([self.tablero[i][i] for i in range(3)]) == jugador * 3:
                return jugador

            if sum([self.tablero[i][2 - i] for i in range(3)]) == jugador * 3:
                return jugador

        # Verifica si hay empate.
        empate = True

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    empate = False

        if empate:
            return 1

        # Si no hay ganador ni empate, sigue el juego.
        return 0         