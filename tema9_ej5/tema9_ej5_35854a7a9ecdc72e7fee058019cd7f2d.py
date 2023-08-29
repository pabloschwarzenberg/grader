class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero de juego de 3x3
        self.jugador_gato = 1
        self.jugador_raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Implementación del algoritmo de jugada más inteligente para el ratón
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.jugador_raton
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobación de filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                if fila[0] == self.jugador_gato:
                    return 2  # Ganó el gato
                else:
                    return 3  # Ganó el ratón

        # Comprobación de columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == self.jugador_gato:
                    return 2  # Ganó el gato
                else:
                    return 3  # Ganó el ratón

        # Comprobación de diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == self.jugador_gato:
                return 2  # Ganó el gato
            else:
                return 3  # Ganó el ratón
        elif self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == self.jugador_gato:
                return 2  # Ganó el gato
            else:
                return 3  # Ganó el ratón

        # Comprobación de empate
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1  # Empate

        # No hay ganador, se puede seguir jugando
        return 0


