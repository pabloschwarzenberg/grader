import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_gato = 1
        self.jugador_raton = -1

    def __repr__(self):
        return str(self.tablero)

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.jugador_gato
            return True
        else:
            return False

    def jugarRaton(self):
        posiciones_disponibles = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    posiciones_disponibles.append((fila, columna))
        
        if len(posiciones_disponibles) > 0:
            fila, columna = random.choice(posiciones_disponibles)
            self.tablero[fila][columna] = self.jugador_raton
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for jugador in [self.jugador_gato, self.jugador_raton]:
            # Comprobar filas
            for fila in range(3):
                if all(posicion == jugador for posicion in self.tablero[fila]):
                    return jugador

            # Comprobar columnas
            for columna in range(3):
                if all(self.tablero[fila][columna] == jugador for fila in range(3)):
                    return jugador

            # Comprobar diagonales
            if self.tablero[0][0] == jugador and self.tablero[1][1] == jugador and self.tablero[2][2] == jugador:
                return jugador
            if self.tablero[0][2] == jugador and self.tablero[1][1] == jugador and self.tablero[2][0] == jugador:
                return jugador

        if all(self.tablero[fila][columna] != 0 for fila in range(3) for columna in range(3)):
            return 1  # Empate

        return 0  # El juego aún no ha terminado

# Ejemplo de uso:
juego = JuegoDelGato()

# Jugar con el gato
juego.jugarGato(0, 0)
juego.jugarGato(0, 1)

# Jugar con el ratón
juego.jugarRaton()

# Mostrar el tablero
print(juego.mostrar_tablero())

# Indicar el estado del juego
print(juego.indicarEstado())
