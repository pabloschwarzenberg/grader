import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Verificar si el ratón puede ganar en el siguiente movimiento
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    if self.indicarEstado() == 3:
                        return True
                    else:
                        self.tablero[fila][columna] = 0

        # Verificar si el gato puede ganar en el siguiente movimiento y bloquearlo
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = 1
                    if self.indicarEstado() == 2:
                        self.tablero[fila][columna] = -1
                        return True
                    else:
                        self.tablero[fila][columna] = 0

        # Jugar de forma aleatoria si no hay jugadas ganadoras
        jugadas_disponibles = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    jugadas_disponibles.append((fila, columna))

        if jugadas_disponibles:
            fila, columna = random.choice(jugadas_disponibles)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                return 2 if fila[0] == 1 else 3

        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Verificar empate
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1

        # No hay ganador y se puede seguir jugando
        return 0


# Ejemplo de uso
if __name__ == "__main__":
    juego = JuegoDelGato()

    # Jugar gato en la posición (1, 1)
    juego.jugarGato(1, 1)

    # Jugar ratón
    juego.jugarRaton()

    # Mostrar el tablero
    tablero = juego.mostrar_tablero()
    for fila in tablero:
        print(fila)

    # Indicar estado del juego
    estado = juego.indicarEstado()
    if estado == 0:
        print("El juego continúa")
    elif estado == 1:
        print("¡Empate!")
    elif estado == 2:
        print("¡Gato gana!")
    elif estado == 3:
        print("¡Ratón gana!")
