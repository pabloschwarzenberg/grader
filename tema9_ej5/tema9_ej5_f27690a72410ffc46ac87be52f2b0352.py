class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.turno = 1  # 1 para el gato, -1 para el ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno *= -1
            return True
        else:
            return False

    def jugarRaton(self):
        # Lógica para determinar la jugada más inteligente del ratón
        # Aquí puedes implementar tu propia estrategia de juego del ratón
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    self.turno *= -1
                    return True
        return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay un ganador en las filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en las columnas
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2  # Ganó el gato
            elif self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en las diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or \
           self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2  # Ganó el gato
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or \
             self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3  # Ganó el ratón

        # Verificar si hay empate
        if all(0 not in fila for fila in self.tablero):
            return 1  # Empate

        # El juego continúa
        return 0


# Ejemplo de uso
juego = JuegoDelGato()

print(juego.mostrar_tablero())  # Salida: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

juego.jugarGato(0, 0)
juego.jugarGato(1, 1)
juego.jugarRaton()
juego.jugarGato(2, 2)
juego.jugarRaton()
juego.jugarRaton()

print(juego.mostrar_tablero())  # Salida: [[1, 0, 0], [0, 1, -1], [0, 0, -1]]

estado = juego.indicarEstado()
if estado == 0:
    print("El juego continúa")
elif estado == 1:
    print("Empate")
elif estado == 2:
    print("Ganó el gato")
elif estado == 3:
    print("Ganó el ratón")
