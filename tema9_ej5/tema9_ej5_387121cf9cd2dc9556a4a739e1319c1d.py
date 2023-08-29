class JuegoDelGato:

    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        fila = 0
        columna = 2
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def indicarEstado(self):
        if self.tablero[0][0] == self.tablero[0][1] == self.tablero[0][2] != 0 or \
                self.tablero[1][0] == self.tablero[1][1] == self.tablero[1][2] != 0 or \
                self.tablero[2][0] == self.tablero[2][1] == self.tablero[2][2] != 0 or \
                self.tablero[0][0] == self.tablero[1][0] == self.tablero[2][0] != 0 or \
                self.tablero[0][1] == self.tablero[1][1] == self.tablero[2][1] != 0 or \
                self.tablero[0][2] == self.tablero[1][2] == self.tablero[2][2] != 0 or \
                self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0 or \
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][0] == 1:
                return 2 
            else:
                return 3  
        elif all(0 not in fila for fila in self.tablero):
            return 1  
        else:
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

         