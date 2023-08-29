class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0] for _ in range(3)]
        self.gato = 1
        self.raton = -1

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        # Implementa aquí la lógica para la jugada más inteligente del ratón
        # Retorna True si pudo jugar y False si no pudo

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for i in range(3):
            # Comprobación de filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == self.gato else 3

            # Comprobación de columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == self.gato else 3

        # Comprobación de diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or (
            self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0
        ):
            return 2 if self.tablero[1][1] == self.gato else 3

        # Comprobación de empate
        if all(cell != 0 for row in self.tablero for cell in row):
            return 1

        return 0


if __name__ == "__main__":
    juego = JuegoDelGato()

    # Ejemplo de juego
    juego.jugarGato(0, 0)
    juego.jugarRaton()
    juego.jugarGato(1, 1)
    juego.jugarRaton()
    juego.jugarGato(2, 2)
    print(juego.mostrar_tablero())

    estado = juego.indicarEstado()
    if estado == 0:
        print("El juego sigue")
    elif estado == 1:
        print("Empate")
    elif estado == 2:
        print("¡Gato ganó!")
    elif estado == 3:
        print("¡Ratón ganó!")
         