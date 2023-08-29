import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        return False
    
    def jugarRaton(self):
        posibles_jugadas = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == 0]
        if posibles_jugadas:
            fila, columna = self.mejorJugada(posibles_jugadas)
            self.tablero[fila][columna] = -1
            return True
        return False
    
    def mejorJugada(self, posibles_jugadas):
        for fila, columna in posibles_jugadas:
            tablero_copia = [fila[:] for fila in self.tablero]
            tablero_copia[fila][columna] = -1
            if self.ganador(tablero_copia) == 3:
                return fila, columna
        for fila, columna in posibles_jugadas:
            tablero_copia = [fila[:] for fila in self.tablero]
            tablero_copia[fila][columna] = 1
            if self.ganador(tablero_copia) == 2:
                return fila, columna
        return random.choice(posibles_jugadas)
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        self.tablero = matriz
    
    def indicarEstado(self):
        ganador = self.ganador(self.tablero)
        if ganador == 0:
            return 0
        elif ganador == -1:
            return 1
        elif ganador == 1:
            return 2
        elif ganador == 3:
            return 3
    
    def ganador(self, tablero):
        for fila in tablero:
            if sum(fila) == 3:
                return 2
            if sum(fila) == -3:
                return 3
        for j in range(3):
            if tablero[0][j] + tablero[1][j] + tablero[2][j] == 3:
                return 2
            if tablero[0][j] + tablero[1][j] + tablero[2][j] == -3:
                return 3
        if tablero[0][0] + tablero[1][1] + tablero[2][2] == 3:
            return 2
        if tablero[0][0] + tablero[1][1] + tablero[2][2] == -3:
            return 3
        if tablero[0][2] + tablero[1][1] + tablero[2][0] == 3:
            return 2
        if tablero[0][2] + tablero[1][1] + tablero[2][0] == -3:
            return 3
        for fila in tablero:
            if 0 in fila:
                return 0
        return -1