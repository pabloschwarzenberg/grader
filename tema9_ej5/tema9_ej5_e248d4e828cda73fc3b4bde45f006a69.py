import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Tablero de juego
        self.jugador_actual = 1  # 1: Gato, -1: Ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        else:
            return False

    def jugarRaton(self):
        # Obtener las coordenadas de las celdas vacías
        celdas_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    celdas_vacias.append((i, j))

        if not celdas_vacias:
            return False

        # Evaluar todas las posibles jugadas del ratón y elegir la mejor
        mejor_jugada = None
        mejor_puntaje = float('-inf')

        for fila, columna in celdas_vacias:
            self.tablero[fila][columna] = -1
            puntaje = self.minimax(0, False)
            self.tablero[fila][columna] = 0

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_jugada = (fila, columna)

        fila, columna = mejor_jugada
        self.tablero[fila][columna] = -1
        self.jugador_actual = 1
        return True

    def minimax(self, profundidad, es_maximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.evaluarEstado()

        if es_maximizador:
            mejor_puntaje = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def indicarEstado(self):
        # Comprobar si hay un ganador en filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                return fila[0]

        # Comprobar si hay un ganador en columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return self.tablero[0][columna]

        # Comprobar si hay un ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return self.tablero[0][2]

        # Comprobar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1  # Empate

        # No hay ganador ni empate
        return 0

    def evaluarEstado(self):
        # Comprobar si hay un ganador en filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                return fila[0]

        # Comprobar si hay un ganador en columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return self.tablero[0][columna]

        # Comprobar si hay un ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return self.tablero[0][2]

        # Comprobar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1  # Empate

        # No hay ganador ni empate
        return 0

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

juego = JuegoDelGato()

