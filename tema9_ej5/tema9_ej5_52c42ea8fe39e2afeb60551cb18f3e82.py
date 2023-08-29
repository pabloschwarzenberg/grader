class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero inicial vacío
        self.jugador_actual = 1  # El jugador actual, 1 para el gato, -1 para el ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1  # Cambiar turno al ratón
            return True
        else:
            return False

    def jugarRaton(self):
        # Buscar la mejor jugada para el ratón (estrategia aleatoria en este caso)
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.jugador_actual = 1  # Cambiar turno al gato
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            return False
        self.tablero = matriz
        return True

    def indicarEstado(self):
        # Verificar si hay un ganador en filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Ganó el gato
            elif self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón

        # Si no hay ganador, verificar si hay empate o se puede seguir jugando
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1  # Empate
        else:
            return 0  # Juego en progreso

# Ejemplo de uso
juego = JuegoDelGato()
print

         