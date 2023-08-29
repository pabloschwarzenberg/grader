class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        simbolos = {-1: 'R', 0: ' ', 1: 'G'}
        lineas = []
        for fila in self.tablero:
            lineas.append('|' + '|'.join([simbolos[celda] for celda in fila]) + '|')
        return '\n'.join(lineas)

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
        lineas = []
        for fila in self.tablero:
            lineas.append(fila)
        for columna in range(3):
            lineas.append([self.tablero[fila][columna] for fila in range(3)])
        lineas.append([self.tablero[i][i] for i in range(3)])
        lineas.append([self.tablero[i][2 - i] for i in range(3)])
        if [1, 1, 1] in lineas:
            return 2
        elif [-1, -1, -1] in lineas:
            return 3
        elif all(celda != 0 for fila in self.tablero for celda in fila):
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
    