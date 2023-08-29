class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return self.mostrar_tablero()

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        if self.indicarEstado() == 0:
            # Buscar una posición vacía en el tablero
            posiciones_vacias = []
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        posiciones_vacias.append((i, j))

            if posiciones_vacias:
                fila, columna = posiciones_vacias[0]
                self.tablero[fila][columna] = -1
                return True
            else:
                return False

    def indicarEstado(self):
        # Comprobar si hay ganador en las filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

        # Comprobar si hay ganador en las columnas
        for i in range(3):
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3

        # Comprobar si hay ganador en las diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or \
                (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3

        # Comprobar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        # No hay ganador ni empate, se puede seguir jugando
        return 0

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         