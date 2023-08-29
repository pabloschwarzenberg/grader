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
        # Encuentra la jugada más inteligente para el ratón (opcional)
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay un ganador en filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en columnas
        for columna in range(3):
            if (
                self.tablero[0][columna] == self.tablero[1][columna]
                == self.tablero[2][columna]
                == 1
            ):
                return 2  # Ganó el gato
            elif (
                self.tablero[0][columna] == self.tablero[1][columna]
                == self.tablero[2][columna]
                == -1
            ):
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en diagonales
        if (
            self.tablero[0][0] == self.tablero[1][1]
            == self.tablero[2][2]
            == 1
            or self.tablero[0][2] == self.tablero[1][1]
            == self.tablero[2][0]
            == 1
        ):
            return 2  # Ganó el gato
        elif (
            self.tablero[0][0] == self.tablero[1][1]
            == self.tablero[2][2]
            == -1
            or self.tablero[0][2] == self.tablero[1][1]
            == self.tablero[2][0]
            == -1
        ):
            return 3  # Ganó el ratón

        # Verificar si hay empate
        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        # Si no hay ganador ni empate, el juego continúa
        return 0


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)

         