import random


class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno = 1

    def __repr__(self):
        tablero_str = ""
        for fila in self.tablero:
            for valor in fila:
                if valor == 0:
                    tablero_str += " "
                elif valor == 1:
                    tablero_str += "X"
                else:
                    tablero_str += "O"
            tablero_str += "\n"
        return tablero_str

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos = self.obtenerMovimientosDisponibles()
        if movimientos:
            mejor_movimiento = self.obtenerMejorMovimiento(movimientos)
            fila, columna = mejor_movimiento
            self.tablero[fila][columna] = -1
            self.turno = 1
            return True
        else:
            return False

    def obtenerMovimientosDisponibles(self):
        movimientos = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos.append((fila, columna))
        return movimientos

    def obtenerMejorMovimiento(self, movimientos):
        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = -1
            if self.verificarGanador(-1):
                self.tablero[fila][columna] = 0
                return fila, columna
            self.tablero[fila][columna] = 0

        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = 1
            if self.verificarGanador(1):
                self.tablero[fila][columna] = 0
                return fila, columna
            self.tablero[fila][columna] = 0

        return random.choice(movimientos)

    def verificarGanador(self, jugador):
        # Filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] == jugador:
                return True

        # Columnas
        for columna in range(3):
            if (
                self.tablero[0][columna]
                == self.tablero[1][columna]
                == self.tablero[2][columna]
                == jugador
            ):
                return True

        # Diagonales
        if (
            self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador
            or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador
        ):
            return True

        return False

    def indicarEstado(self):
        if self.verificarGanador(1):
            return 2  # Ganó el gato
        elif self.verificarGanador(-1):
            return 3  # Ganó el ratón
        elif self.obtenerMovimientosDisponibles():
            return 0  # El juego continúa
        else:
            return 1  # Empate

    def cargar_tablero(self, matriz):
        self.tablero = matriz

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
    estado = juego.indicarEstado()
    if estado == 1:
        print("¡Empate!")
    elif estado == 2:
        print("¡Ganó el gato!")
    elif estado == 3:
        print("¡Ganó el ratón!")
