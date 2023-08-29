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
        return False

    def jugarRaton(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))

        if not posiciones_vacias:
            return False

        fila, columna = self.obtenerMejorJugada(posiciones_vacias)
        self.tablero[fila][columna] = self.raton
        return True

    def obtenerMejorJugada(self, posiciones_vacias):
        # Simulación aleatoria de jugadas para determinar la mejor opción
        mejor_jugada = None
        mejor_puntaje = float('-inf')

        for fila, columna in posiciones_vacias:
            self.tablero[fila][columna] = self.raton
            puntaje = self.simularJuego()

            if puntaje > mejor_puntaje:
                mejor_jugada = (fila, columna)
                mejor_puntaje = puntaje

            self.tablero[fila][columna] = 0  # Revertir la jugada

        return mejor_jugada

    def simularJuego(self):
        estado = self.indicarEstado()
        if estado != 0:
            return estado

        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))

        if not posiciones_vacias:
            return 0

        fila, columna = random.choice(posiciones_vacias)
        self.tablero[fila][columna] = self.gato
        puntaje = -self.simularJuego()
        self.tablero[fila][columna] = 0  # Revertir la jugada

        return puntaje

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in self.tablero:
            if fila == [self.gato, self.gato, self.gato]:
                return 2 if self.gato == 1 else 3
            if fila == [self.raton, self.raton, self.raton]:
                return 3 if self.raton == -1 else 2

        for columna in range(3):
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [self.gato] * 3:
                return 2 if self.gato == 1 else 3
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [self.raton] * 3:
                return 3 if self.raton == -1 else 2

        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [self.gato] * 3 or \
                [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [self.gato] * 3:
            return 2 if self.gato == 1 else 3

        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [self.raton] * 3 or \
                [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [self.raton] * 3:
            return 3 if self.raton == -1 else 2

        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        return 0
         