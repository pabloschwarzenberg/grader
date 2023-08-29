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
        if self.indicarEstado() != 0:
            return False

        mejor_puntaje = -float('inf')
        mejor_jugada = None

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[i][j] = 0

                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (i, j)

        if mejor_jugada is not None:
            self.tablero[mejor_jugada[0]][mejor_jugada[1]] = -1
            return True
        else:
            return False

    def minimax(self, profundidad, esMaximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return self.obtenerPuntaje(estado, profundidad)

        if esMaximizador:
            mejor_puntaje = -float('inf')

            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(profundidad + 1, False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)

            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')

            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(profundidad + 1, True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)

            return mejor_puntaje

    def obtenerPuntaje(self, estado, profundidad):
        if estado == 1:
            return 0
        elif estado == 2:
            return 10 - profundidad
        elif estado == 3:
            return profundidad - 10

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

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

        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return 0

        return 1


# Ejemplo de uso:
juego = JuegoDelGato()

# Cargar tablero
tablero = [[0, 0, -1], [0, 1, 0], [1, 1, 0]]
juego.cargar_tablero(tablero)

# Jugar ratón
juego.jugarRaton()

# Mostrar el tablero actual
tablero = juego.mostrar_tablero()
for fila in tablero:
    print(fila)

# Obtener el estado del juego
estado = juego.indicarEstado()
print("Estado del juego:", estado)
