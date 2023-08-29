import random

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
        # Buscar la jugada más inteligente del ratón
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True

        return False

    def indicarEstado(self):
        # Comprobar filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            if fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Ganó el gato
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ganó el ratón

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 2  # Ganó el gato
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 3  # Ganó el ratón
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón

        # Comprobar empate
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1  # Empate

        return 0  # El juego sigue

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
