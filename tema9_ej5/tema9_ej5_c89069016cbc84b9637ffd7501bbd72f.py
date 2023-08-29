class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]  # Tablero vacío

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:  # Verificar si la celda está vacía
            self.tablero[fila][columna] = 1  # Asignar el gato
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_jugada = self.encontrarMejorJugada()
        if mejor_jugada:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1  # Asignar el ratón
            return True
        else:
            return False

    def encontrarMejorJugada(self):
        # Implementa aquí la lógica para encontrar la mejor jugada del ratón
        # Puedes usar algoritmos de inteligencia artificial como Minimax o Alpha-Beta Pruning

        # Ejemplo: Elige la primera celda vacía encontrada
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
        for fila in self.tablero:
            if all(cell == 1 for cell in fila):  # El gato gana en una fila
                return 2
            elif all(cell == -1 for cell in fila):  # El ratón gana en una fila
                return 3

        for columna in range(3):
            if all(self.tablero[fila][columna] == 1 for fila in range(3)):  # El gato gana en una columna
                return 2
            elif all(self.tablero[fila][columna] == -1 for fila in range(3)):  # El ratón gana en una columna
                return 3

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1:  # El gato gana en la diagonal principal
            return 2
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1:  # El ratón gana en la diagonal principal
            return 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:  # El gato gana en la diagonal secundaria
            return 2
        elif self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:  # El ratón gana en la diagonal secundaria
            return 3

        if all(cell != 0 for fila in self.tablero for cell in fila):  # Tablero lleno, empate
            return 1

        return 0
