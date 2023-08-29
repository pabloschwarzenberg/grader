class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero vacío

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Buscar la jugada más inteligente del ratón (puedes implementar la lógica aquí)
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay un ganador en las filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                if fila[0] == 1:
                    return 2  # Ganó el gato
                else:
                    return 3  # Ganó el ratón

        # Verificar si hay un ganador en las columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == 1:
                    return 2  # Ganó el gato
                else:
                    return 3  # Ganó el ratón

        # Verificar si hay un ganador en las diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0 or \
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[1][1] == 1:
                return 2  # Ganó el gato
            else:
                return 3  # Ganó el ratón

        # Verificar si hay empate
        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        # Si no hay ganador ni empate, el juego continúa
        return 0
