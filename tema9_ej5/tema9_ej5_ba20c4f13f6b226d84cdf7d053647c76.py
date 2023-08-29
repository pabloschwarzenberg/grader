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
        movimientos_disponibles = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos_disponibles.append((fila, columna))

        if len(movimientos_disponibles) > 0:
            fila, columna = random.choice(movimientos_disponibles)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def indicarEstado(self):
        ganador = 0
        # Verificar filas
        for fila in self.tablero:
            if fila.count(1) == 3:
                ganador = 2
            elif fila.count(-1) == 3:
                ganador = 3

        # Verificar columnas
        for columna in range(3):
            if (
                self.tablero[0][columna] == self.tablero[1][columna]
                == self.tablero[2][columna]
            ):
                if self.tablero[0][columna] == 1:
                    ganador = 2
                elif self.tablero[0][columna] == -1:
                    ganador = 3

        # Verificar diagonales
        if (
            self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]
            or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]
        ):
            if self.tablero[1][1] == 1:
                ganador = 2
            elif self.tablero[1][1] == -1:
                ganador = 3

        if ganador == 0 and self.tablero_lleno():
            ganador = 1

        return ganador

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

    def tablero_lleno(self):
        for fila in self.tablero:
            if 0 in fila:
                return False
        return True


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)