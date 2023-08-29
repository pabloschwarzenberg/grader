class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]
        self.turno = 1

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            s += " ".join([str(casilla) for casilla in fila]) + "\n"
        return s

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1

    def jugarRaton(self):
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero[fila])):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.turno = 1
                    return

    def indicarEstado(self):
        for fila in self.tablero:
            if all(casilla == 1 for casilla in fila):
                return 1
            elif all(casilla == -1 for casilla in fila):
                return -1
        for columna in range(len(self.tablero[0])):
            if all(self.tablero[fila][columna] == 1 for fila in range(len(self.tablero))):
                return 1
            elif all(self.tablero[fila][columna] == -1 for fila in range(len(self.tablero))):
                return -1
        if all(self.tablero[i][i] == 1 for i in range(len(self.tablero))):
            return 1
        elif all(self.tablero[i][i] == -1 for i in range(len(self.tablero))):
            return -1
        if all(self.tablero[i][len(self.tablero) - i - 1] == 1 for i in range(len(self.tablero))):
            return 1
        elif all(self.tablero[i][len(self.tablero) - i - 1] == -1 for i in range(len(self.tablero))):
            return -1
        return 0

    def cargar_tablero(self, tablero):
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
