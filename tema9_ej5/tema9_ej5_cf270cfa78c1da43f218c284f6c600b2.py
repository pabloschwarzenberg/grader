class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            s += " | ".join(["X" if celda == 1 else "O" if celda == -1 else " " for celda in fila]) + "\n"
            s += "-" * 9 + "\n"
        return s

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntuacion = -float("inf")
        mejor_fila = -1
        mejor_columna = -1

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntuacion = self.minimax(1, False)
                    self.tablero[fila][columna] = 0

                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        mejor_fila = fila
                        mejor_columna = columna

        if mejor_fila != -1 and mejor_columna != -1:
            self.tablero[mejor_fila][mejor_columna] = -1
            return True
        else:
            return False

    def minimax(self, profundidad, es_maximizador):
        resultado = self.indicarEstado()

        if resultado != 0:
            return resultado

        if es_maximizador:
            mejor_puntuacion = -float("inf")
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntuacion = self.minimax(profundidad + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)
            return mejor_puntuacion
        else:
            mejor_puntuacion = float("inf")
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntuacion = self.minimax(profundidad + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)
            return mejor_puntuacion

    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == 1 else 3

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return 0

        return 1

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
         