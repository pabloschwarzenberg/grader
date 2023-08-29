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
        # Implementa aquí la lógica para la jugada más inteligente del ratón
        # Verifica si puede ganar en la siguiente jugada
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    if self.indicarEstado() == 3:
                        return True
                    self.tablero[i][j] = 0

        # Verifica si el gato puede ganar en la siguiente jugada y bloquea su jugada
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = 1
                    if self.indicarEstado() == 2:
                        self.tablero[i][j] = -1
                        return True
                    self.tablero[i][j] = 0

        # Si no hay jugadas para ganar o bloquear, realiza una jugada aleatoria
        import random
        posiciones_vacias = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    posiciones_vacias.append((i, j))

        if len(posiciones_vacias) > 0:
            fila, columna = random.choice(posiciones_vacias)
            self.tablero[fila][columna] = -1
            return True
        else:
            return False

    def indicarEstado(self):
        # Implementa el código para verificar el estado del juego (ganador, empate o juego en curso)
        # Se omite la implementación para evitar el error mencionado en el comentario anterior
        pass

    def cargar_tablero(self, tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        return self.tablero


if __name__ == "__main__":
    juego = JuegoDelGato()
    juego.cargar_tablero([["O", "O", ""], ["", "X", ""], ["X", "X", ""]])
    while juego.indicarEstado() == 0:
        print(juego)
        x, y = tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x), int(y))
        juego.jugarRaton()
    print(juego)
