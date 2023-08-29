import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero vacío
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Verificar si hay una jugada ganadora para el ratón
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    if self.indicarEstado() == 3:
                        return True
                    else:
                        self.tablero[fila][columna] = 0
        
        # Si no hay jugada ganadora, hacer una jugada aleatoria
        jugada_valida = False
        while not jugada_valida:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            if self.tablero[fila][columna] == 0:
                self.tablero[fila][columna] = self.raton
                jugada_valida = True
                return True

        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay un ganador
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == self.gato else 3
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == self.gato else 3
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == self.gato else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == self.gato else 3

        # Verificar si hay empate
        for fila in self.tablero:
            if 0 in fila:
                return 0

        return 1