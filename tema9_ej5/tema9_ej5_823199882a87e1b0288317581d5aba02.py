class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Tablero de juego
        self.gato = 1  # Representación del gato en el tablero
        self.raton = -1  # Representación del ratón en el tablero

    def __repr__(self):
        return self.mostrar_tablero()

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:  # Verifica si la celda está vacía
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        fila, columna = self.obtener_jugada_optima()
        if fila is not None and columna is not None:
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def mostrar_tablero(self):
        return [[self.tablero[i][j] for j in range(3)] for i in range(3)]

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        ganador = self.verificar_ganador()
        if ganador is not None:
            return ganador
        elif self.verificar_empate():
            return 1
        else:
            return 0

    def verificar_ganador(self):
        # Verifica filas
        for fila in self.tablero:
            if fila.count(self.gato) == 3:
                return 2  # Gato gana
            elif fila.count(self.raton) == 3:
                return 3  # Ratón gana

        # Verifica columnas
        for columna in range(3):
            if [self.tablero[i][columna] for i in range(3)].count(self.gato) == 3:
                return 2  # Gato gana
            elif [self.tablero[i][columna] for i in range(3)].count(self.raton) == 3:
                return 3  # Ratón gana

        # Verifica diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == self.gato else 3
        elif self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == self.gato else 3

        return None

    def verificar_empate(self):
        return all(celda != 0 for fila in self.tablero for celda in fila)

    def obtener_jugada_optima(self):
        # Estrategia del ratón: juega en la primera celda vacía disponible
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return fila, columna
        return None, None


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)

         