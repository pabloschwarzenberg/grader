class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.turno = 1

    def __repr__(self):
        return "\n".join([" ".join(map(str, fila)) for fila in self.tablero])

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1
            return True
        return False

    def jugarRaton(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.turno = 1
                    return True
        return False

    def indicarEstado(self):
        for fila in self.tablero:
            if all(elem == 1 for elem in fila):
                return 2  # Ganó el gato (jugador 1)
            if all(elem == -1 for elem in fila):
                return 3  # Ganó el ratón (jugador -1)

        for columna in range(3):
            if all(self.tablero[fila][columna] == 1 for fila in range(3)):
                return 2
            if all(self.tablero[fila][columna] == -1 for fila in range(3)):
                return 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 2
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3

        if all(elem != 0 for fila in self.tablero for elem in fila):
            return 1  # Empate

        return 0  # El juego continúa

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
        if juego.jugarGato(int(x), int(y)):
            juego.jugarRaton()
    print(juego)

         