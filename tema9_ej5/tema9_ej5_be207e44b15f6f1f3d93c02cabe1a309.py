import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0 for _ in range(3)] for _ in range(3)]
        self.gato = 1
        self.raton = -1

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        posibles_jugadas = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posibles_jugadas.append((i,j))
        if len(posibles_jugadas) > 0:
            fila,columna = random.choice(posibles_jugadas)
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self,matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            if sum(self.tablero[i]) == 3*self.gato:
                return 2
            elif sum(self.tablero[i]) == 3*self.raton:
                return 3
        for j in range(3):
            if sum([self.tablero[i][j] for i in range(3)]) == 3*self.gato:
                return 2
            elif sum([self.tablero[i][j] for i in range(3)]) == 3*self.raton:
                return 3
        if sum([self.tablero[i][i] for i in range(3)]) == 3*self.gato or sum([self.tablero[i][2-i] for i in range(3)]) == 3*self.gato:
            return 2
        elif sum([self.tablero[i][i] for i in range(3)]) == 3*self.raton or sum([self.tablero[i][2-i] for i in range(3)]) == 3*self.raton:
            return 3
        elif sum([sum(self.tablero[i]) != 0 for i in range(3)]) == 3:
            return 1
        else:
            return 0
