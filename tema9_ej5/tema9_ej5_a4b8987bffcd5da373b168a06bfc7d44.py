class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

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

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        lineas = []
        lineas.extend(self.tablero)
        lineas.extend([[self.tablero[j][i] for j in range(3)] for i in range(3)])
        lineas.append([self.tablero[i][i] for i in range(3)])
        lineas.append([self.tablero[i][2-i] for i in range(3)])

        if any(sum(linea) == 3 for linea in lineas):
            return 2
        elif any(sum(linea) == -3 for linea in lineas):
            return 3
        elif all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1
        else:
            return 0
juego = JuegoDelGato()
juego.jugarGato(0, 0)
juego.jugarRaton()
print(juego.mostrar_tablero())
