class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Tablero vacío
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        jugada = self.obtenerMejorJugada()
        if jugada is not None:
            fila, columna = jugada
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def obtenerMejorJugada(self):
        # Implementa aquí tu lógica para calcular la mejor jugada del ratón
        # Puedes usar cualquier algoritmo o estrategia que desees
        # En este ejemplo, el ratón jugará en la primera celda vacía que encuentre
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
        # Verificar si hay ganador en filas
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != 0:
                return 2 if fila[0] == self.gato else 3

        # Verificar si hay ganador en columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == self.gato else 3

        # Verificar si hay ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == self.gato else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == self.gato else 3

        # Verificar si hay empate
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1

        # El juego continúa
        return 0
  