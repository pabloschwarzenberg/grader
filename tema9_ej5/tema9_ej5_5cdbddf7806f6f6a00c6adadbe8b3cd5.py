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
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(row) == 3 for row in matriz):
            self.tablero = matriz

    def indicarEstado(self):
        # Comprobar filas
        for fila in self.tablero:
            if all(cell == 1 for cell in fila):
                return 2  # Ganó el gato
            if all(cell == -1 for cell in fila):
                return 3  # Ganó el ratón

        # Comprobar columnas
        for columna in range(3):
            if all(self.tablero[fila][columna] == 1 for fila in range(3)):
                return 2  # Ganó el gato
            if all(self.tablero[fila][columna] == -1 for fila in range(3)):
                return 3  # Ganó el ratón

        # Comprobar diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1) or (
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1):
            return 2  # Ganó el gato
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1) or (
                self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1):
            return 3  # Ganó el ratón

        # Comprobar empate
        if all(cell != 0 for fila in self.tablero for cell in fila):
            return 1  # Empate

        # El juego aún no ha terminado
        return 0

    def __repr__(self):
        return "\n".join([" ".join(map(str, fila)) for fila in self.tablero])


# Ejemplo de uso
juego = JuegoDelGato()
print(juego.mostrar_tablero())

juego.jugarGato(1, 1)
juego.jugarRaton()
juego.jugarGato(0, 0)
juego.jugarRaton()
juego.jugarGato(2, 2)
juego.jugarRaton()

print(juego.mostrar_tablero())
print(juego.indicarEstado())
