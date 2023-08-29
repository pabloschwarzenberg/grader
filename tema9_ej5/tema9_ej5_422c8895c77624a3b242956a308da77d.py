import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0 for _ in range(3)] for _ in range(3)]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))
        if len(posiciones_vacias) == 0:
            return False

        # Verificar si el gato puede ganar en el próximo movimiento
        for fila, columna in posiciones_vacias:
            self.tablero[fila][columna] = self.gato
            if self.indicarEstado() == 2:
                self.tablero[fila][columna] = self.raton
                return True
            self.tablero[fila][columna] = 0

        # Jugar aleatoriamente si no se encontró una posición para bloquear al gato
        fila, columna = random.choice(posiciones_vacias)
        self.tablero[fila][columna] = self.raton
        return True

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            if sum(self.tablero[i]) == 3:
                return 2
            elif sum(self.tablero[i]) == -3:
                return 3

        for j in range(3):
            if sum([self.tablero[i][j] for i in range(3)]) == 3:
                return 2
            elif sum([self.tablero[i][j] for i in range(3)]) == -3:
                return 3

        if sum([self.tablero[i][i] for i in range(3)]) == 3 or sum([self.tablero[2-i][i] for i in range(3)]) == 3:
            return 2
        elif sum([self.tablero[i][i] for i in range(3)]) == -3 or sum([self.tablero[2-i][i] for i in range(3)]) == -3:
            return 3

        if all([x != 0 for row in self.tablero for x in row]):
            return 1
        else:
            return 0

         