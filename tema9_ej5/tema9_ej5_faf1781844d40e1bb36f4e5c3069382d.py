class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True
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
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1
        return 0

    def cargar_tablero(self, tablero):
        if len(tablero) != 3 or any(len(row) != 3 for row in tablero):
            raise ValueError("El tablero debe ser una matriz de 3x3")
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        if not juego.jugarGato(int(x), int(y)):
            print("Jugada inválida. Inténtalo nuevamente.")
        else:
            if juego.indicarEstado() == 0:
                if juego.jugarRaton():
                    print("Turno del ratón:")
                else:
                    print("No hay más movimientos posibles. ¡Empate!")
            else:
                break

    estado = juego.indicarEstado()
    print(juego)
    if estado == 1:
        print("¡Empate!")
    elif estado == 2:
        print("¡El gato ha ganado!")
    elif estado == 3:
        print("¡El ratón ha ganado!")
