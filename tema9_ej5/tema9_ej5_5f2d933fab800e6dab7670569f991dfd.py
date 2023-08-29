import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turno = 1  # 1 para el gato, -1 para el ratón

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno = -1  # Cambiar turno al ratón
            return True
        else:
            return False

    def jugarRaton(self):
        # Obtener todas las posiciones vacías
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))

        if posiciones_vacias:
            # Elegir una posición al azar para el ratón
            fila, columna = random.choice(posiciones_vacias)
            self.tablero[fila][columna] = -1
            self.turno = 1  # Cambiar turno al gato
            return True
        else:
            return False

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        # Verificar si hay ganador en filas
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3

        # Verificar si hay ganador en columnas
        for j in range(3):
            if self.tablero[0][j] == self.tablero[1][j] == self.tablero[2][j] != 0:
                return 2 if self.tablero[0][j] == 1 else 3

        # Verificar si hay ganador en diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3

        # Verificar si hay empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1

        # El juego aún no ha terminado
        return 0

    def __repr__(self):
        return str(self.tablero)


if __name__ == "__main__":
    juego = JuegoDelGato()
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = map(int, input("Ingresa tu jugada (fila,columna): ").split(","))
        while not juego.jugarGato(x, y):
            print("Movimiento inválido. Intenta nuevamente.")
            x, y = map(int, input("Ingresa tu jugada (fila,columna): ").split(","))
        juego.jugarRaton()
    print(juego)

    estado = juego.indicarEstado()
    if estado == 1:
        print("¡Empate!")
    elif estado == 2:
        print("¡Ganó el Gato!")
    elif estado == 3:
        print("¡Ganó el Ratón!")
