class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Inicializar tablero vacío
        self.turno_gato = True  # True si es el turno del gato, False si es el turno del ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
            return True
        else:
            return False

    def jugarRaton(self):
        if self.turno_gato:
            return False

        mejor_jugada = None
        mejor_puntaje = -float('inf')

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(0, True)
                    self.tablero[fila][columna] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (fila, columna)

        if mejor_jugada:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1
            self.turno_gato = True
            return True
        else:
            return False

    def minimax(self, profundidad, es_turno_gato):
        estado = self.indicarEstado()

        if estado != 0:
            return estado

        if es_turno_gato:
            mejor_puntaje = -float('inf')
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

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar columnas
        for columna in range(3):
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [1, 1, 1]:
                return 2  # Ganó el gato
            elif [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar diagonales
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [1, 1, 1] or [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [1, 1, 1]:
            return 2  # Ganó el gato
        elif [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [-1, -1, -1] or [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [-1, -1, -1]:
            return 3  # Ganó el ratón

        # Verificar empate
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1  # Empate

        # No hay ganador y se puede seguir jugando
        return 0
