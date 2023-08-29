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
        movimientos_posibles = []
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    movimientos_posibles.append((fila, columna))
        
        if not movimientos_posibles:
            return False
        
        # Realizar una jugada aleatoria si solo queda una casilla vacía
        if len(movimientos_posibles) == 1:
            fila, columna = movimientos_posibles[0]
            self.tablero[fila][columna] = self.raton
            return True
        
        # Verificar si el ratón puede ganar en el siguiente movimiento
        for fila, columna in movimientos_posibles:
            self.tablero[fila][columna] = self.raton
            estado = self.indicarEstado()
            self.tablero[fila][columna] = 0
            if estado == 3:
                self.tablero[fila][columna] = self.raton
                return True
        
        # Verificar si el gato puede ganar en el siguiente movimiento y bloquearlo
        for fila, columna in movimientos_posibles:
            self.tablero[fila][columna] = self.gato
            estado = self.indicarEstado()
            self.tablero[fila][columna] = 0
            if estado == 2:
                self.tablero[fila][columna] = self.raton
                return True
        
        # Realizar una jugada aleatoria
        fila, columna = random.choice(movimientos_posibles)
        self.tablero[fila][columna] = self.raton
        return True

    def mostrar_tablero(self):
        return self.tablero

    def cargar_tablero(self, matriz):
        self.tablero = matriz

    def indicarEstado(self):
        for fila in range(3):
            # Verificar filas
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2]:
                if self.tablero[fila][0] == self.gato:
                    return 2
                elif self.tablero[fila][0] == self.raton:
                    return 3

            # Verificar columnas
            if self.tablero[0][fila] == self.tablero[1][fila] == self.tablero[2][fila]:
                if self.tablero[0][fila] == self.gato:
                    return 2
                elif self.tablero[0][fila] == self.raton:
                    return 3

        # Verificar diagonales
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2]:
            if self.tablero[0][0] == self.gato:
                return 2
            elif self.tablero[0][0] == self.raton:
                return 3

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0]:
            if self.tablero[0][2] == self.gato:
                return 2
            elif self.tablero[0][2] == self.raton:
                return 3

        # Verificar empate
        if all(all(casilla != 0 for casilla in fila) for fila in self.tablero):
            return 1

        # Juego en curso
        return 0
