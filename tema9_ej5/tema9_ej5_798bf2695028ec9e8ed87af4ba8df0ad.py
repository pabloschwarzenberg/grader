import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos.append((fila, columna))

        if movimientos:
            fila, columna = random.choice(movimientos)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz
        else:
            raise ValueError("La matriz debe ser de tamaño 3x3.")

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

        # No hay ganador, se puede seguir jugando
        return 0
