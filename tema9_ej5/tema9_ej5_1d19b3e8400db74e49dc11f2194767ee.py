class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]
        self.turno_gato = True

    def __repr__(self):
        rep = ""
        for fila in self.tablero:
            rep += " ".join(str(celda) for celda in fila) + "\n"
        return rep

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
            return True
        else:
            return False

    def jugarRaton(self):
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))

        if len(posiciones_vacias) > 0:
            fila, columna = posiciones_vacias[0]
            self.tablero[fila][columna] = -1
            self.turno_gato = True
            return True
        else:
            return False

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        if self.tableroCompleto():
            return 1

        return 0

    def tableroCompleto(self):
        for fila in self.tablero:
            if 0 in fila:
                return False
        return True

if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = input("Ingresa tu jugada (fila,columna): ").split(",")
        if juego.jugarGato(int(x), int(y)):
            juego.jugarRaton()
        else:
            print("¡Movimiento inválido! Intenta de nuevo.")
    print(juego)
