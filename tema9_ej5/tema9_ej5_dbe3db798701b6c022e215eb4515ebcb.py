class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_gato = 1
        self.jugador_raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Implementa la lógica para que el ratón juegue de forma inteligente
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.jugador_raton
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and len(matriz[0]) == 3:
            self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                if fila[0] == self.jugador_gato:
                    return 2
                else:
                    return 3

        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == self.jugador_gato:
                    return 2
                else:
                    return 3

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == self.jugador_gato:
                return 2
            else:
                return 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == self.jugador_gato:
                return 2
            else:
                return 3

        # Verificar empate
        empate = True
        for fila in self.tablero:
            if 0 in fila:
                empate = False
                break
        if empate:
            return 1

        # No hay ganador, se puede seguir jugando
        return 0