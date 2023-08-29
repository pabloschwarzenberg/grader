import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Encontrar las celdas vacías
        celdas_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    celdas_vacias.append((i, j))

        if celdas_vacias:
            fila, columna = random.choice(celdas_vacias)
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(fila) == 3 for fila in matriz):
            self.tablero = matriz

    def indicarEstado(self):
        for jugador in [self.gato, self.raton]:
            # Verificar filas
            for i in range(3):
                if self.tablero[i] == [jugador, jugador, jugador]:
                    return 2 if jugador == self.gato else 3

            # Verificar columnas
            for j in range(3):
                if [self.tablero[i][j] for i in range(3)] == [jugador, jugador, jugador]:
                    return 2 if jugador == self.gato else 3

            # Verificar diagonales
            if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:
                return 2 if jugador == self.gato else 3
            if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:
                return 2 if jugador == self.gato else 3

        # Verificar si es empate
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1

        # El juego puede continuar
        return 0
