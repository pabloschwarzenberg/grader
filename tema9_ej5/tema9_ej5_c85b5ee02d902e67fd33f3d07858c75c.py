class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno_gato = True  # True: turno del gato, False: turno del ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            if self.turno_gato:
                self.tablero[fila][columna] = 1  # Gato
            else:
                self.tablero[fila][columna] = -1  # Ratón
            self.turno_gato = not self.turno_gato
            return True
        else:
            return False

    def jugarRaton(self):
        if not self.turno_gato:
            mejores_jugadas = []  # Lista de tuplas (fila, columna) de las mejores jugadas posibles
            mejor_puntaje = float('-inf')  # Inicializar con un valor muy bajo

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        # Calcular puntaje de la jugada
                        self.tablero[fila][columna] = -1  # Simular jugada del ratón
                        puntaje = self.minimax(0, False)
                        self.tablero[fila][columna] = 0  # Deshacer jugada del ratón

                        if puntaje > mejor_puntaje:
                            mejor_puntaje = puntaje
                            mejores_jugadas = [(fila, columna)]
                        elif puntaje == mejor_puntaje:
                            mejores_jugadas.append((fila, columna))

            if len(mejores_jugadas) > 0:
                fila, columna = random.choice(mejores_jugadas)
                self.tablero[fila][columna] = -1  # Ratón
                self.turno_gato = not self.turno_gato
                return True

        return False

    def minimax(self, profundidad, esMaximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.obtenerPuntaje(estado, profundidad)

        if esMaximizador:
            mejor_puntaje = float('-inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1  # Ratón
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[fila][columna] = 0  # Deshacer jugada del ratón
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1  # Gato
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[fila][columna] = 0  # Deshacer jugada del gato
                        mejor_puntaje = min(mejor_puntaje,
