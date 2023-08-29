import random

class JuegoDelGato:

    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]

    def __repr__(self):
        s = ""
        for fila in self.tablero:
            for valor in fila:
                if valor == 0:
                    s += " "
                elif valor == 1:
                    s += "X"
                elif valor == -1:
                    s += "O"
                s += "|"
            s = s[:-1] + "\n"
        return s

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False

    def jugarRaton(self):
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

    def indicarEstado(self):
        for fila in self.tablero:
            if fila == [1, 1, 1]:
                return 2  # Gana el gato
            elif fila == [-1, -1, -1]:
                return 3  # Gana el ratón
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == 1:
                return 2
            elif self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] == -1:
                return 3
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == 1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == 1:
            return 2
        elif self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == -1 or self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == -1:
            return 3
        for fila in self.tablero:
            if 0 in fila:
                return 0  # Juego en curso
        return 1  # Empate

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(fila) == 3 for fila in matriz):
            self.tablero = matriz

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.cargar_tablero([[-1, -1, 0], [0, 1, 0], [1, 1, 0]])
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
