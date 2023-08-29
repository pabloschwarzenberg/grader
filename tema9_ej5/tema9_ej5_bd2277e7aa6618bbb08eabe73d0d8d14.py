class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_actual = 1  # 1 para el gato, -1 para el ratón
        self.movimientos = 0

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            self.movimientos += 1
            return True
        else:
            return False

    def jugarRaton(self):
        if self.movimientos >= 9:
            return False

        mejores_puntajes = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    puntaje = self.evaluarMovimiento(fila, columna, -1)
                    mejores_puntajes.append((puntaje, fila, columna))

        mejores_puntajes.sort(reverse=True, key=lambda x: x[0])
        mejor_puntaje = mejores_puntajes[0]
        mejor_fila = mejor_puntaje[1]
        mejor_columna = mejor_puntaje[2]

        self.tablero[mejor_fila][mejor_columna] = -1
        self.jugador_actual = 1
        self.movimientos += 1
        return True

    def evaluarMovimiento(self, fila, columna, jugador):
        self.tablero[fila][columna] = jugador
        estado = self.indicarEstado()
        self.tablero[fila][columna] = 0
        return estado

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobar filas
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2]:
                if self.tablero[fila][0] == 1:
                    return 2  # Gana el gato
                elif self.tablero[fila][0] == -1:
                    return 3  # Gana el ratón

        # Comprobar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna]:
                if self.tablero[0][columna] == 1:
                    return 2  # Gana el gato
                elif self.tablero[0][columna] == -1:
                    return 3  # Gana el ratón

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == 1:
                return 2  # Gana el gato
            elif self.tablero[0][0] == -1:
                return
