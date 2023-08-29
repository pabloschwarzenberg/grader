class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]  # Tablero inicial

    def __repr__(self):
        return self.mostrar_tablero()

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:  # Verificar si la celda está vacía
            self.tablero[fila][columna] = 1  # Asignar el valor del gato
            return True
        else:
            return False

    def jugarRaton(self):
        # En este ejemplo, el ratón simplemente elegirá la primera celda vacía que encuentre
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay ganador en filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                return 2 if fila[0] == 1 else 3

        # Verificar si hay ganador en columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != 0:
                return 2 if self.tablero[0][j] == 1 else 3

        # Verificar si hay ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Verificar si hay empate
        for fila in self.tablero:
            if 0 in fila:
                return 0

        return 1


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
