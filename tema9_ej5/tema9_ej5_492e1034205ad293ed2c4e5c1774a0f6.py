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
        # Verificar si hay una casilla vacía
        casillas_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    casillas_vacias.append((i, j))

        if casillas_vacias:
            fila, columna = random.choice(casillas_vacias)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) != 3 or len(matriz[0]) != 3:
            raise ValueError("La matriz debe ser de tamaño 3x3")
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

        # Verificar columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != 0:
                return 2 if self.tablero[0][j] == 1 else 3

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Verificar empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        # Juego en curso
        return 0
