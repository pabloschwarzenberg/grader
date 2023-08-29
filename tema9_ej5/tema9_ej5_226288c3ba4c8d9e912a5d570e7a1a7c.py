import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
        opciones = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    opciones.append((i, j))
        
        if opciones:
            fila, columna = self.mejor_jugada(opciones)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def mejor_jugada(self, opciones):
        # Estrategia básica: seleccionar una jugada al azar
        return random.choice(opciones)

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def indicarEstado(self):
        # Comprobar si hay un ganador en las filas
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Ganó el gato
            elif fila == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobar si hay un ganador en las columnas
        for j in range(3):
            columna = [self.tablero[i][j] for i in range(3)]
            if columna == [1, 1, 1]:
                return 2  # Ganó el gato
            elif columna == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Comprobar si hay un ganador en las diagonales
        diagonal_principal = [self.tablero[i][i] for i in range(3)]
        if diagonal_principal == [1, 1, 1]:
            return 2  # Ganó el gato
        elif diagonal_principal == [-1, -1, -1]:
            return 3  # Ganó el ratón

        diagonal_secundaria = [self.tablero[i][2-i] for i in range(3)]
        if diagonal_secundaria == [1, 1, 1]:
            return 2  # Ganó el gato
        elif diagonal_secundaria == [-1, -1, -1]:
            return 3  # Ganó el ratón

        # Comprobar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1  # Empate

        # Si no hay ganador ni empate, el juego continúa
        return 0


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)