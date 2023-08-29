class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_actual = 1

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            for celda in fila:
                if celda == 0:
                    s += " "
                elif celda == 1:
                    s += "X"
                else:
                    s += "O"
                s += "|"
            s = s[:-1] + "\n-----\n"
        return s[:-6]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_puntaje = float('-inf')
        mejor_movimiento = None
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[i][j] = 0
                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_movimiento = (i, j)
        if mejor_movimiento is not None:
            fila, columna = mejor_movimiento
            self.tablero[fila][columna] = -1
            self.jugador_actual = 1
            return True
        else:
            return False

    def minimax(self, profundidad, es_maximizador):
        resultado = self.indicarEstado()
        if resultado != 0:
            return resultado

        if es_maximizador:
            mejor_puntaje = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return self.tablero[i][0]
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return self.tablero[0][i]
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return self.tablero[0][0]
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return self.tablero[0][2]
        if all(celda != 0 for fila in self.tablero for celda in fila):
            return 1  # Empate
        return 0  # Juego en progreso

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
