import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno_gato = True

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            if self.turno_gato:
                self.tablero[fila][columna] = 1
            else:
                self.tablero[fila][columna] = -1
            self.turno_gato = not self.turno_gato
            return True
        else:
            return False

    def jugarRaton(self):
        movimientos = self.obtenerMovimientosPosibles()
        if len(movimientos) > 0:
            mejor_movimiento = self.obtenerMejorMovimiento(movimientos)
            fila, columna = mejor_movimiento
            self.tablero[fila][columna] = -1
            self.turno_gato = not self.turno_gato
            return True
        else:
            return False

    def obtenerMovimientosPosibles(self):
        movimientos = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos.append((fila, columna))
        return movimientos

    def obtenerMejorMovimiento(self, movimientos):
        # Simplemente se elige un movimiento al azar en este ejemplo
        return random.choice(movimientos)

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in range(3):
            # Comprobar filas
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == 1 else 3
        for columna in range(3):
            # Comprobar columnas
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3
        # Comprobar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3
        # Comprobar empate
        if self.tableroCompleto():
            return 1
        # No hay ganador y se puede seguir jugando
        return 0

    def tableroCompleto(self):
        for fila in self.tablero:
            if 0 in fila:
                return False
        return True


# Ejemplo de uso
juego = JuegoDelGato()

# Jugar gato
juego.jugarGato(0, 0)
juego.jugarGato(1, 1)
juego.jugarGato(2, 2)

# Jugar ratón
juego.jugarRaton()

# Mostrar tablero
tablero = juego.mostrar_tablero()
for fila in tablero:
    print(fila)

# Obtener estado del juego
estado = juego.indicarEstado()
print("Estado del juego:", estado)
