class JuegoDelGato:
    def __init__(self):
        self.tablero = [[-1, -1, 0], [0, 1, 0], [1, 1, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        # Implementa la lógica para que el ratón juegue de forma inteligente
        # según la configuración actual del tablero
        # Puedes usar una estrategia simple o implementar un algoritmo más complejo

        # Aquí se presenta un ejemplo de una estrategia aleatoria para el ratón
        import random
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.tablero[i][j] == 0]
        if empty_cells:
            fila, columna = random.choice(empty_cells)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay un ganador en filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Ganó el gato
            elif self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón

        # Verificar si hay empate
        if all(all(celda != 0 for celda in fila) for fila in self.tablero):
            return 1  # Empate

        # Si no hay ganador ni empate, se puede seguir jugando
        return 0


if __name__ == "__main__":
    juego = JuegoDelGato()
   
         