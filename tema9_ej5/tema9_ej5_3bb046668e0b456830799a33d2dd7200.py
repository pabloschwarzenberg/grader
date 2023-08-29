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
        mejor_jugada = None
        mejor_puntaje = float('-inf')

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = self.raton
                    puntaje = self.minimax(0, False)
                    self.tablero[i][j] = 0

                if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (i, j)

        if mejor_jugada:
            self.tablero[mejor_jugada[0]][mejor_jugada[1]] = self.raton
            return True
        else:
            return False

    def minimax(self, profundidad, esMaximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.obtenerPuntaje(estado)

        if esMaximizador:
            mejor_puntaje = float('-inf')

            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.gato
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(puntaje, mejor_puntaje)

            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')

            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = self.raton
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(puntaje, mejor_puntaje)

            return mejor_puntaje

    def obtenerPuntaje(self, estado):
        if estado == 1:
            return 0
        elif estado == 2:
            return 1
        elif estado == 3:
            return -1

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in self.tablero:
            if fila.count(fila[0]) == len(fila) and fila[0] != 0:
                if fila[0] == self.gato:
                    return 2
                else:
                    return 3

        for columna in range(3):
            if (
                self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna]
                and self.tablero[0][columna] != 0
            ):
                if self.tablero[0][columna] == self.gato:
                    return 2
