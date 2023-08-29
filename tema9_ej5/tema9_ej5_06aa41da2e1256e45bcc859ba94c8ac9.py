import random

class JuegoDelGato:
 
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno_gato = True

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
            return True
        else:
            return False

    def jugarRaton(self):
        if not self.turno_gato:
            movimientos = []
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        movimientos.append((i, j))

            if movimientos:
                fila, columna = random.choice(movimientos)
                self.tablero[fila][columna] = -1
                self.turno_gato = True
                return True
            else:
                return False
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                if self.tablero[i][0] == 1:
                    return 2
                else:
                    return 3
            elif self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                if self.tablero[0][i] == 1:
                    return 2
                else:
                    return 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                return 2
            else:
                return 3

        if self.tablero[2][0] == self.tablero[1][1] == self.tablero[0][2] != 0:
            if self.tablero[2][0] == 1:
                return 2
            else:
                return 3

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return 0

        return 1

if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego.mostrar_tablero())
        if juego.turno_gato:
            x, y = tuple(input("Ingresa tu jugada como gato (fila,columna): ").split(","))
            if juego.jugarGato(int(x), int(y)):
                print("Jugada válida.")
            else:
                print("Jugada inválida. Inténtalo de nuevo.")
        else:
            if juego.jugarRaton():
                print("Turno del ratón.")

    print(juego.mostrar_tablero())
    estado = juego.indicarEstado()
    if estado == 1:
        print("Empate.")
    elif estado == 2:
        print("Ganó el gato.")
    elif estado == 3:
        print("

