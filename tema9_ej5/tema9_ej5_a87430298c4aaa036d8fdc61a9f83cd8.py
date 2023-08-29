#La idea es que se pueda jugar contra el computador, y que sea interesante jugar contra él…

#Para lograrlo, crea la clase JuegoDelGato, con los siguientes métodos:

#jugarGato(self,fila,columna): asigna la fila y columna indicada del tablero al gato, retornando True si lo pudo hacer y False si es que no.
#jugarRaton(self): el ratón debe escoger la jugada más inteligente según la configuración del tablero. El método debe retornar True si pudo jugar y False si es que no.
#mostrar_tablero(self): debe retornar una matriz de 3x3 donde un 0 es una celda vacía, un 1 es un gato y un -1 es un ratón (no es necesario que uses internamente esa codificación).
#cargar_tablero(self,matriz): reemplaza tu tablero de acuerdo a la matriz de 3x3 recibida como parámetro con valores 0, 1 y -1.
#indicarEstado(self): debe retornar 0 si no hay ganador pero se puede seguir jugando, 1 si hay empate, 2 si ganó el gato, 3 si ganó el ratón.

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
                    posiciones_vacias.append((i,j))
        if len(posiciones_vacias) == 0:
            return False
        else:
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