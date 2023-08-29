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
        jugada_realizada = False

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    if self.indicarEstado() == 3:
                        jugada_realizada = True
                        break
                    else:
                        self.tablero[fila][columna] = 0

            if jugada_realizada:
                break

        if not jugada_realizada:
            import random

            while True:
                fila = random.randint(0, 2)
                columna = random.randint(0, 2)

                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    jugada_realizada = True
                    break

        return jugada_realizada

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == 1 else 3

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3

        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or \
           (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3

        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1

        return 0