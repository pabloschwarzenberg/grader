class JuegoDelGato:
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
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))

        if len(movimientos) == 0:
            return False

        mejor_movimiento = self.encontrarMejorMovimiento(movimientos)
        fila, columna = mejor_movimiento
        self.tablero[fila][columna] = -1
        return True

    def encontrarMejorMovimiento(self, movimientos):
        mejor_movimiento = movimientos[0]
        mejor_puntaje = -float("inf")

        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = -1
            puntaje = self.minimax(0, False)
            self.tablero[fila][columna] = 0

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento

        return mejor_movimiento

    def minimax(self, profundidad, esTurnoGato):
        estado = self.indicarEstado()
        if estado != 0:
            return estado - profundidad

        if esTurnoGato:
            mejor_puntaje = -float("inf")
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float("inf")
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            # Filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

            # Columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1
