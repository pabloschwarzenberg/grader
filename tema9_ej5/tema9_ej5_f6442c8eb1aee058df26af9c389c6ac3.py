class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return "\n".join(" ".join(str(valor) for valor in fila) for fila in self.tablero)

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def indicarEstado(self):
        # Verificar filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Gana el gato
            if fila == [-1, -1, -1]:
                return 3  # Gana el ratón

        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Gana el gato
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Gana el ratón

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Gana el gato
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Gana el ratón

        # Verificar empate
        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1  # Empate

        return 0  # El juego no ha terminado

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
