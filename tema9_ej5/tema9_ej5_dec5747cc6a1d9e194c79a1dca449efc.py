import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 1, 0], [1, 1, 0]]
        self.gato_x = random.randint(0, 2)
        self.gato_y = random.randint(0, 2)
        self.raton_x = 1
        self.raton_y = 1

    def __repr__(self):
        return str(self.mostrar_tablero())

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.gato_x = fila
            self.gato_y = columna
            return True
        else:
            return False

    def jugarRaton(self):
        jugada_realizada = False

        # Comprobamos si hay una celda vacía en el tablero
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    self.raton_x = i
                    self.raton_y = j
                    jugada_realizada = True
                    break

            if jugada_realizada:
                break

        return jugada_realizada

    def indicarEstado(self):
        if self.gato_x == self.raton_x and self.gato_y == self.raton_y:
            return 1  # Empate
        elif self.gato_x == 1 and self.gato_y == 1:
            return 2  # Gato ganó
        elif self.raton_x == 1 and self.raton_y == 1:
            return 3  # Ratón ganó
        else:
            return 0  # Se puede seguir jugando

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)