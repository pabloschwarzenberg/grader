class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno = 1  # 1: turno del gato, -1: turno del ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1
            return True
        else:
            return False

    def jugarRaton(self):
        if self.turno == -1:
            mejor_jugada = self.obtenerMejorJugada()
            if mejor_jugada:
                fila, columna = mejor_jugada
                self.tablero[fila][columna] = -1
                self.turno = 1
                return True
        return False

    def obtenerMejorJugada(self):
        # Implementa aquí la lógica para obtener la mejor jugada del ratón
        # Puedes utilizar algoritmos de búsqueda, como el algoritmo Minimax

        # En este ejemplo, simplemente se elige la primera celda vacía disponible
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return fila, columna
        return None

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Revisa si hay algún ganador
        for i in range(3):
            # Revisa las filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

            # Revisa las columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3

        # Revisa las diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or \
           (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3

        # Revisa si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        # Si no hay ganador ni empate, se puede seguir jugando
        return 0


# Ejemplo de uso
juego = JuegoDelGato()

# Juega el gato en la fila 0, columna 0
juego.jugarGato(0, 0)

# Juega el ratón
juego.jugarRaton()

# Muestra el tablero
tablero = juego.mostrar_tablero()
for fila in tablero:
    print(fila)

# Carga un tablero predef

