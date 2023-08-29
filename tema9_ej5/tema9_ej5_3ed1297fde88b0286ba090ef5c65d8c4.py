import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return ""

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        opciones = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    if self.indicarEstado() == 3:  # Ratón ganaría en su próximo movimiento
                        self.tablero[fila][columna] = 0  # Deshacer movimiento
                        return True
                    self.tablero[fila][columna] = 0  # Deshacer movimiento
                    opciones.append((fila, columna))

        if opciones:
            fila, columna = random.choice(opciones)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def indicarEstado(self):
        for fila in range(3):
            # Comprobar si hay una fila completa para el gato
            if self.tablero[fila] == [1, 1, 1]:
                return 2  # Gato ganó
            # Comprobar si hay una fila completa para el ratón
            if self.tablero[fila] == [-1, -1, -1]:
                return 3  # Ratón ganó

        for columna in range(3):
            # Comprobar si hay una columna completa para el gato
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [1, 1, 1]:
                return 2  # Gato ganó
            # Comprobar si hay una columna completa para el ratón
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [-1, -1, -1]:
                return 3  # Ratón ganó

        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:
            return 2  # Gato ganó
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:
            return 3  # Ratón ganó
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Gato ganó
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ratón ganó

        # Comprobar si hay espacios vacíos en el tablero
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return 0  # Juego aún en progreso

        # Si no hay ganador y no hay espacios vacíos, es un empate
        return 1  # Empate

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

juego = JuegoDelGato()
while juego.indicarEstado() == 0:
    print(juego.mostrar_tablero())
    x, y = map(int, input("Ingresa tu jugada: ").split(","))
    juego.jugarGato(x, y)
    juego.jugarRaton()

print(juego.mostrar_tablero())
