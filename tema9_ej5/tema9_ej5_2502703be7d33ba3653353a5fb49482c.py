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
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def indicarEstado(self):
        # Verificar filas
        for fila in self.tablero:
            if fila.count(1) == 3:
                return 2  # Gato ganó
            if fila.count(-1) == 3:
                return 3  # Ratón ganó

        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Gato ganó
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ratón ganó

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or \
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Gato ganó
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or \
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ratón ganó

        # Verificar empate
        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        # El juego puede seguir
        return 0

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return [[valor for valor in fila] for fila in self.tablero]


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)


         