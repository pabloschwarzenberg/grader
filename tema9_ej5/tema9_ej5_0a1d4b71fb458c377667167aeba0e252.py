class JuegoDelGato:

    def __init__(self):
        self.estado = 0
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.dificultad = 0

    def __repr__(self):
        mostrar = ""
        tablero = self.mostrar_tablero()
        for i in range(len(tablero)):
            mostrar += str(tablero[i]) + "\n"
        if self.estado == 3:
            print("Gano el Raton")
        elif self.estado == 2:
            print("Gano el Gato")
        elif self.estado == 1:
            print("Es un empate")
        else:
            print("Sigan jugando")
        return mostrar

    def jugarGato(self,  fila, columna):
        tablero = self.tablero
        if tablero[columna][fila] == 0:
            jugada = True
            tablero[columna][fila] = 1
        else:
            return False

        if jugada:
            self.cargar_tablero(tablero)
        return jugada

    def jugarRaton(self):
        tablero = self.tablero
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))

        if not movimientos:
            return False

        mejor_movimiento = None
        mejor_puntaje = -9999

        for movimiento in movimientos:
            fila, columna = movimiento
            self.tablero[fila][columna] = -1
            puntaje = self.minimax(0, True, self.dificultad)
            self.tablero[fila][columna] = 0

            if puntaje > mejor_puntaje:
                mejor_puntaje = puntaje
                mejor_movimiento = movimiento

        if mejor_movimiento:
            fila, columna = mejor_movimiento
            tablero[fila][columna] = -1
            self.cargar_tablero(tablero)
            return True
        else:
            return False

    def minimax(self, posicion, es_maximizador, depth):
        if depth == 0:
            return posicion
        if self.indicarEstado() == 3:
            posicion += 2
            return posicion
        elif self.indicarEstado() == 2:
            posicion -= 100
            return posicion
        elif self.indicarEstado() == 0:
            posicion -= 1
        elif self.indicarEstado() == 1:
            posicion -= 2
            return posicion

        if es_maximizador:
            mejor_puntaje = 9999
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(posicion, False, depth - 1)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = -99999
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(posicion, True, depth - 1)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje

    def indicarEstado(self):
        h = False
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                self.estado = 2
                return 2  # Gato ganó
            else:
                self.estado = 3
                return 3  # Ratón ganó

        elif self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == 1:
                self.estado = 2
                return 2  # Gato ganó
            else:
                self.estado = 3
                return 3  # Ratón ganó

        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                if self.tablero[i][0] == 1:
                    self.estado = 2
                    return 2  # Gato ganó
                else:
                    self.estado = 3
                    return 3  # Ratón ganó

            elif self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                if self.tablero[0][i] == 1:
                    self.estado = 2
                    return 2  # Gato ganó
                else:
                    self.estado = 3
                    return 3  # Ratón ganó
        for columna in range(len(self.tablero)):
            for fila in self.tablero[columna]:
                if fila == 0:
                    h = True
                    break
        if not h:
            return 1  # Empate
        self.estado = 0
        return 0

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.dificultad = int(input("Ingrese la dificultad (1-9): "))
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)