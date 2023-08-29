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
        # Verificar si hay jugadas ganadoras para el ratón
        for i in range(3):
            if self.tablero[i] == [-1, -1, 0]:
                self.tablero[i][2] = -1
                return True
            elif self.tablero[i] == [-1, 0, -1]:
                self.tablero[i][1] = -1
                return True
            elif self.tablero[i] == [0, -1, -1]:
                self.tablero[i][0] = -1
                return True

            if [self.tablero[0][i], self.tablero[1][i], self.tablero[2][i]] == [-1, -1, 0]:
                self.tablero[2][i] = -1
                return True
            elif [self.tablero[0][i], self.tablero[1][i], self.tablero[2][i]] == [-1, 0, -1]:
                self.tablero[1][i] = -1
                return True
            elif [self.tablero[0][i], self.tablero[1][i], self.tablero[2][i]] == [0, -1, -1]:
                self.tablero[0][i] = -1
                return True

        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [-1, -1, 0]:
            self.tablero[2][2] = -1
            return True
        elif [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [-1, 0, -1]:
            self.tablero[1][1] = -1
            return True
        elif [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [0, -1, -1]:
            self.tablero[0][0] = -1
            return True

        if [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [-1, -1, 0]:
            self.tablero[2][0] = -1
            return True
        elif [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [-1, 0, -1]:
            self.tablero[1][1] = -1
            return True
        elif [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [0, -1, -1]:
            self.tablero[0][2] = -1
            return True

        # Si no hay jugadas ganadoras, el ratón juega en la primera celda vacía
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    self.tablero[i][j] = -1
                    return True

        return False

    def indicarEstado(self):
        # Verificar si hay un ganador en filas
        for i in range(3):
            if self.tablero[i] == [1, 1, 1]:
                return 2  # Ganó el gato
            elif self.tablero[i] == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en columnas
        for i in range(3):
            if [self.tablero[0][i], self.tablero[1][i], self.tablero[2][i]] == [1, 1, 1]:
                return 2  # Ganó el gato
            elif [self.tablero[0][i], self.tablero[1][i], self.tablero[2][i]] == [-1, -1, -1]:
                return 3  # Ganó el ratón

        # Verificar si hay un ganador en diagonales
        if [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [1, 1, 1]:
            return 2  # Ganó el gato
        elif [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]] == [-1, -1, -1]:
            return 3  # Ganó el ratón

        if [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [1, 1, 1]:
            return 2  # Ganó el gato
        elif [self.tablero[0][2], self.tablero[1][1], self.tablero[2][0]] == [-1, -1, -1]:
            return 3  # Ganó el ratón

        # Verificar si hay empate
        empate = True
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    empate = False
                    break
        if empate:
            return 1  # Empate

        return 0  # El juego no ha terminado

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