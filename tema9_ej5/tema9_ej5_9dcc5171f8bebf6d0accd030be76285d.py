class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.ganador = 0
        self.turno_gato = True

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            if self.turno_gato:
                self.tablero[fila][columna] = 1
                self.turno_gato = False
            else:
                self.tablero[fila][columna] = -1
                self.turno_gato = True
            return True
        else:
            return False

    def jugarRaton(self):
        if self.ganador == 0:
            # Verificar si hay jugada ganadora para el ratón
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        if self.indicarEstado() == 3:
                            self.turno_gato = True
                            return True
                        else:
                            self.tablero[i][j] = 0

            # Jugar en una celda vacía aleatoria
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        self.turno_gato = True
                        return True

        return False

    def indicarEstado(self):
        # Verificar filas
        for i in range(3):
            if self.tablero[i][0] != 0 and self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2]:
                self.ganador = self.tablero[i][0]
                return self.ganador

        # Verificar columnas
        for j in range(3):
            if self.tablero[0][j] != 0 and self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j]:
                self.ganador = self.tablero[0][j]
                return self.ganador

        # Verificar diagonales
        if self.tablero[0][0] != 0 and self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            self.ganador = self.tablero[0][0]
            return self.ganador

        if self.tablero[0][2] != 0 and self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]:
            self.ganador = self.tablero[0][2]
            return self.ganador

        # Verificar empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            self.ganador = 1
            return self.ganador

        # El juego continúa
        return 0

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
