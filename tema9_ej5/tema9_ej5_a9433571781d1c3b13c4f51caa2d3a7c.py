class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero inicial vacío
        self.turno = 1  # 1: turno del gato, -1: turno del ratón

    def __repr__(self):
        # Representación visual del tablero
        simbolos = {0: ' ', 1: 'X', -1: 'O'}
        filas = []
        for fila in self.tablero:
            filas.append('|'.join([simbolos[valor] for valor in fila]))
        return '\n-+-+-\n'.join(filas)

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1
            return True
        else:
            return False

    def jugarRaton(self):
        # Estrategia simple: juega en la primera celda vacía disponible
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.turno = 1
                    return True
        return False

    def indicarEstado(self):
        # Verificar si hay un ganador o empate
        ganador = 0
        for jugador in [1, -1]:
            if (
                (self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2] == jugador) or
                (self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2] == jugador) or
                (self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2] == jugador) or
                (self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0] == jugador) or
                (self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1] == jugador) or
                (self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2] == jugador) or
                (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador) or
                (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador)
            ):
                ganador = jugador

        # Verificar si hay empate
        empate = True
        for fila in self.tablero:
            if 0 in fila:
                empate = False
                break

        if ganador != 0:
            return 2 if ganador == 1 else 3
        elif empate:
            return 1
        else:
            return 0

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