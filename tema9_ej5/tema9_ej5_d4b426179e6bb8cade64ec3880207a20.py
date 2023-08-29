import random

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
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))
        
        if len(movimientos) > 0:
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
            raise ValueError("La matriz debe tener dimensiones 3x3.")

    def indicarEstado(self):
        for i in range(3):
            # Filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

            # Columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3

        # Diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or \
           (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3

        # Empate
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1

        # Juego en curso
        return 0
         