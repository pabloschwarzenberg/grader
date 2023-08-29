import random

class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.ganador = 0  # 0: No hay ganador, 1: Empate, 2: Gato, 3: Ratón

    def __repr__(self):
        return f"Tablero del juego:\n{self.tablero}"

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 2
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
            fila, columna = random.choice(opciones)
            self.tablero[fila][columna] = 3
            return True
        else:
            return False

    def indicarEstado(self):
        for jugador in [2, 3]:
            # Comprobar filas y columnas
            for i in range(3):
                if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == jugador:
                    self.ganador = jugador
                    return jugador

                if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] == jugador:
                    self.ganador = jugador
                    return jugador

            # Comprobar diagonales
            if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:
                self.ganador = jugador
                return jugador

            if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:
                self.ganador = jugador
                return jugador

        # Comprobar empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            self.ganador = 1  # Empate
            return 1

        return 0

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero

if __name__ == "__main__":
    juego = JuegoDelGato()

    while juego.indicarEstado() == 0:
        print(juego)
        x, y = map(int, input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(x, y)
        juego.jugarRaton()

    print(juego)
    estado = juego.indicarEstado()
    if estado == 1:
        print("¡Es un empate!")
    elif estado == 2:
        print("¡El gato ha ganado!")
    elif estado == 3:
        print("¡El ratón ha ganado!")
