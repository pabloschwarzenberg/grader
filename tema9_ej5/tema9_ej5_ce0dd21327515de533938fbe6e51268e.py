class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Lógica para determinar la jugada más inteligente del ratón
        # Aquí debes implementar tu estrategia de juego para el ratón
        # Puedes usar algoritmos de búsqueda, minimax, etc.
        # Por simplicidad, vamos a hacer una jugada aleatoria en este ejemplo
        import random

        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))

        if posiciones_vacias:
            fila, columna = random.choice(posiciones_vacias)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Comprobar si hay algún ganador en filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                if self.tablero[i][0] == 1:
                    return 2  # Gato gana
                else:
                    return 3  # Ratón gana

        # Comprobar si hay algún ganador en columnas
        for i in range(3):
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                if self.tablero[0][i] == 1:
                    return 2  # Gato gana
                else:
                    return 3  # Ratón gana

        # Comprobar si hay algún ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                return 2  # Gato gana
            else:
                return 3  # Ratón gana

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == 1:
                return 2  # Gato gana
            else:
                return 3  # Ratón gana

        # Comprobar si hay empate
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    return 0  # El juego no ha terminado

        return 1  # Empate
