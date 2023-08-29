import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.gato = 1
        self.raton = -1

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Comprobar si el gato puede ganar en la siguiente jugada
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = self.gato
                    if self.indicarEstado() == 2:
                        self.tablero[i][j] = self.raton
                        return True
                    else:
                        self.tablero[i][j] = 0

        # Bloquear las jugadas del gato
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = self.gato
                    if self.indicarEstado() == 2:
                        self.tablero[i][j] = self.raton
                        return True
                    else:
                        self.tablero[i][j] = 0

        # Realizar una jugada aleatoria
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))
        
        if movimientos:
            fila, columna = random.choice(movimientos)
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def indicarEstado(self):
        for fila in self.tablero:
            if all(elemento == self.gato for elemento in fila):
                return 2  # Gato ha ganado

        for columna in range(3):
            if all(fila[columna] == self.gato for fila in self.tablero):
                return 2  # Gato ha ganado

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == self.gato:
            return 2  # Gato ha ganado

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == self.gato:
            return 2  # Gato ha ganado

        if all(elemento != 0 for fila in self.tablero for elemento in fila):
            return 1  # Empate

        return 0  # El juego puede continuar

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.cargar_tablero([['O', 'O', ' '], [' ', 'X', ' '], ['X', 'X', ' ']])

    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
