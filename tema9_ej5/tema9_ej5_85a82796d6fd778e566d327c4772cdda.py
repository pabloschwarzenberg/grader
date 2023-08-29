class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno_gato = True

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            s += " ".join(str(valor) for valor in fila) + "\n"
        return s

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_jugada = self.obtenerMejorJugada()
        if mejor_jugada:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1
            self.turno_gato = True
            return True
        else:
            return False

    def indicarEstado(self):
        if self.hayGanador(1):
            return 2  # Ganó el gato
        elif self.hayGanador(-1):
            return 3  # Ganó el ratón
        elif self.empate():
            return 1  # Empate
        else:
            return 0  # El juego continua

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(fila) == 3 for fila in matriz):
            self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

    def obtenerMejorJugada(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    if self.hayGanador(-1):
                        self.tablero[fila][columna] = 0
                        return fila, columna
                    self.tablero[fila][columna] = 0
        return None

    def hayGanador(self, jugador):
        # Comprobación de filas
        for fila in self.tablero:
            if fila.count(jugador) == 3:
                return True

        # Comprobación de columnas
        for columna in range(3):
            if [self.tablero[fila][columna] for fila in range(3)].count(jugador) == 3:
                return True

        # Comprobación de diagonales
        if (
            self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador
            or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador
        ):
            return True

        return False

    def empate(self):
        for fila in self.tablero:
            if 0 in fila:
                return False
        return True


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
