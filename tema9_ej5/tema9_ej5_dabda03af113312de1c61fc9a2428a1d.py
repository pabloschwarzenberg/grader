class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos_posibles = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos_posibles.append((i, j))

        if movimientos_posibles:
            fila, columna = movimientos_posibles[0]
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobar filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobar columnas
        for columna in range(3):
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [1, 1, 1]:
                return 2  # Ganó el gato
            elif [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobar diagonales
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [1, 1, 1] or [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [1, 1, 1]:
            return 2  # Ganó el gato
        elif [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [-1, -1, -1] or [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [-1, -1, -1]:
            return 3  # Ganó el ratón

        # Comprobar empate
        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        # Si no hay ganador ni empate, se puede seguir jugando
        return 0

         