import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador = 1
        self.ganador = 0

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador
            self.jugador = -1 if self.jugador == 1 else 1
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos_posibles = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos_posibles.append((i, j))

        # Comprobar si el ratón puede ganar en el siguiente movimiento
        for movimiento in movimientos_posibles:
            fila, columna = movimiento
            self.tablero[fila][columna] = -1
            if self.indicarEstado() == 3:  # Ratón ganaría
                self.tablero[fila][columna] = 0
                self.jugarGato(fila, columna)
                return True
            else:
                self.tablero[fila][columna] = 0

        # Comprobar si el gato puede ganar en el siguiente movimiento y bloquear
        for movimiento in movimientos_posibles:
            fila, columna = movimiento
            self.tablero[fila][columna] = 1
            if self.indicarEstado() == 2:  # Gato ganaría
                self.tablero[fila][columna] = -1
                self.jugarGato(fila, columna)
                return True
            else:
                self.tablero[fila][columna] = 0

        # Jugar en una posición aleatoria si no hay jugadas ganadoras
        if movimientos_posibles:
            fila, columna = random.choice(movimientos_posibles)
            self.tablero[fila][columna] = -1
            self.jugarGato(fila, columna)
            return True
        else:
            return False

    def indicarEstado(self):
        # Comprobar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                self.ganador = fila[0]
                return self.ganador

        # Comprobar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                self.ganador = self.tablero[0][columna]
                return self.ganador

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            self.ganador = self.tablero[0][0]
            return self.ganador

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            self.ganador = self.tablero[0][2]
            return self.ganador

        # Comprobar empate
        empate = True
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    empate = False
                    break
        if empate:
            self.ganador = 1  # Empate
            return self.ganador

        # No hay ganador, se puede seguir jugando
        return 0

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.cargar_tablero([[0, 0, -1], [0, 1, 0], [1, 1, 0]])  # Cargar tablero especificado

    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()

    print(juego)
    if juego.indicarEstado() == 1:
        print("¡Empate!")
    elif juego.indicarEstado() == 2:
        print("¡Ganó el gato!")
    elif juego.indicarEstado() == 3:
        print("¡Ganó el ratón!")
