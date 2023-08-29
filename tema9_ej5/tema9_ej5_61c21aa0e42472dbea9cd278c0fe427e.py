class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]
        self.estado = 0

    def __repr__(self):
        s = ""
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                s += "{0: >5} ".format(self.tablero[i][j])
            s += "\n"
        return s

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.estado = 0

    def jugarRaton(self):
        if self.tablero[0][0] == -1 and self.tablero[0][1] == -1 and self.tablero[0][2] == 0:
            self.tablero[0][2] = -1
            self.estado = 3

    def indicarEstado(self):
            return self.estado

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
