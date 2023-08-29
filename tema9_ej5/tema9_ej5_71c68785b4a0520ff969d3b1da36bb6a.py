class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        jugada_realizada = False
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    if self.indicarEstado() == 3:
                        jugada_realizada = True
                        break
                    else:
                        self.tablero[fila][columna] = 0

            if jugada_realizada:
                break

        return jugada_realizada

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar filas
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2]:
                if self.tablero[fila][0] == self.gato:
                    return 2
                elif self.tablero[fila][0] == self.raton:
                    return 3

        # Verificar columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna]:
                if self.tablero[0][columna] == self.gato:
                    return 2
                elif self.tablero[0][columna] == self.raton:
                    return 3

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == self.gato:
                return 2
            elif self.tablero[0][0] == self.raton:
                return 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]:
            if self.tablero[0][2] == self.gato:
                return 2
            elif self.tablero[0][2] == self.raton:
                return 3

        # Verificar empate
        empate = True
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    empate = False
                    break
        if empate:
            return 1

        # Si no hay ganador ni empate, se puede seguir jugando
        return 0


if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         