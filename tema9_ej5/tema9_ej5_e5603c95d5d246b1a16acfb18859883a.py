class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0] * 3 for _ in range(3)]

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Implementa aquí la lógica para que el ratón juegue de forma inteligente
        # Puedes usar cualquier estrategia que consideres adecuada

        # Ejemplo: jugar en la primera celda vacía que encuentre
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
        # Comprueba si hay un ganador en el tablero
        # Retorna 0 si no hay ganador pero se puede seguir jugando
        # Retorna 1 si hay empate
        # Retorna 2 si ganó el gato
        # Retorna 3 si ganó el ratón

        # Comprobación de filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            if fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobación de columnas
        for columna in range(3):
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [1, 1, 1]:
                return 2  # Ganó el gato
            if [self.tablero[0][columna], self.tablero[1][columna], self.tablero[2][columna]] == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobación de diagonales
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [1, 1, 1] or \
                [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [1, 1, 1]:
            return 2  # Ganó el gato
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [-1, -1, -1] or \
                [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [-1, -1, -1]:
            return 3  # Ganó el ratón

        # Comprobación de empate
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1  # Empate

        return 0  # No hay ganador aún, se puede seguir jugando

         