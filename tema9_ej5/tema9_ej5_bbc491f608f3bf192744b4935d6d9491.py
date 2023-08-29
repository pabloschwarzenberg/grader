class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        return False

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                if self.tablero[i][0] == 1:
                    return 2
                else:
                    return 3

            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                if self.tablero[0][i] == 1:
                    return 2
                else:
                    return 3

        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            if self.tablero[1][1] == 1:
                return 2
            else:
                return 3

        is_full = all(all(cell != 0 for cell in row) for row in self.tablero)
        if is_full:
            return 1

        return 0

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        x = int(x)
        y = int(y)
        if juego.jugarGato(x, y):
            juego.jugarRaton()
    print(juego)