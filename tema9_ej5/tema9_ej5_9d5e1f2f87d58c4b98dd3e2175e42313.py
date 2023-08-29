class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return str(self.tablero)

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
        # Verificar si hay algún ganador en las filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

        # Verificar si hay algún ganador en las columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != 0:
                return 2 if self.tablero[0][j] == 1 else 3

        # Verificar si hay algún ganador en las diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Verificar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        # Si no hay ganador ni empate, se puede seguir jugando
        return 0

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = input("Ingresa tu jugada (fila,columna): ").split(",")
        if juego.jugarGato(int(x), int(y)):
            juego.jugarRaton()
    print(juego)
