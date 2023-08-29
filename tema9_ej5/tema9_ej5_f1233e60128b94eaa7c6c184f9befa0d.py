import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_gato = 1
        self.jugador_raton = -1

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_gato
            return True
        else:
            return False

    def jugarRaton(self):
        posiciones_vacias = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    posiciones_vacias.append((fila, columna))

        if posiciones_vacias:
            fila, columna = random.choice(posiciones_vacias)
            self.tablero[fila][columna] = self.jugador_raton
            return True
        else:
            return False

    def indicarEstado(self):
        ganador = 0

        # Verificar filas
        for fila in self.tablero:
            if fila.count(self.jugador_gato) == 3:
                ganador = 2
            elif fila.count(self.jugador_raton) == 3:
                ganador = 3

        # Verificar columnas
        for columna in range(3):
            if (
                self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == self.jugador_gato
            ):
                ganador = 2
            elif (
                self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == self.jugador_raton
            ):
                ganador = 3

        # Verificar diagonales
        if (
            self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == self.jugador_gato
            or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == self.jugador_gato
        ):
            ganador = 2
        elif (
            self.tablero[0][0]
