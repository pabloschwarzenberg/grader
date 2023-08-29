import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]

    def __repr__(self):
        return "\n".join(" ".join(str(celda) for celda in fila) for fila in self.tablero)

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos = self.obtenerMovimientosPosibles()

        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = -1
            if self.indicarEstado() == 3:
                return True
            else:
                self.tablero[fila][columna] = 0

        if movimientos:
            fila, columna = random.choice(movimientos)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def indicarEstado(self):
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                return 2 if fila[0] == 1 else 3

        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        if all(fila.count(0) == 0 for fila in self.tablero):
            return 1

        return 0

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

    def obtenerMovimientosPosibles(self):
        movimientos = []

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos.append((fila, columna))

        return movimientos


if __name__ == "__main__":
    juego = JuegoDelGato()

    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()

    print(juego)
    estado = juego.indicarEstado()

    if estado == 1:
        print("Empate")
    elif estado == 2:
        print("Ganó el gato")
    elif estado == 3:
        print("Ganó el ratón")
