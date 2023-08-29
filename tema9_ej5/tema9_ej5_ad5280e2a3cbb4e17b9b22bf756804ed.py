class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gato = 1
        self.raton = -1

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntuacion = float('-inf')
        mejor_movimiento = None

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    puntuacion = self.minimax(0, False)
                    self.tablero[fila][columna] = 0

                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        mejor_movimiento = (fila, columna)

        if mejor_movimiento:
            self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = self.raton
            return True
        else:
            return False

    def minimax(self, depth, isMaximizing):
        resultado = self.indicarEstado()

        if resultado != 0:
            return resultado - depth

        if isMaximizing:
            mejor_puntuacion = float('-inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = self.gato
                        puntuacion = self.minimax(depth + 1, False)
                        self.tablero[fila][columna] = 0

                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)

            return mejor_puntuacion

        else:
            mejor_puntuacion = float('inf')

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = self.raton
                        puntuacion = self.minimax(depth + 1, True)
                        self.tablero[fila][columna] = 0

                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)

            return mejor_puntuacion

    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == self.gato else 3

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == self.gato else 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == self.gato else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == self.gato else 3

        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1

        return 0

    def cargar_tablero(self, tablero):
        if len(tablero) == 3 and all(len(fila) == 3 for fila in tablero):
            self.tablero = tablero

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
