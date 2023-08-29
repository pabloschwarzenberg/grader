class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
        self.gato = 1
        self.raton = -1

    def __repr__(self):
        representacion = ""
        for fila in self.tablero:
            for valor in fila:
                if valor == 0:
                    representacion += " "
                elif valor == 1:
                    representacion += "X"
                else:
                    representacion += "O"
                representacion += " | "
            representacion = representacion[:-2] + "\n"  
            representacion += "---------\n"
        return representacion[:-10]  

    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        mejor_jugada = None
        mejor_puntuacion = float('-inf')
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = self.raton
                    puntuacion = self.minimax(0, False)
                    self.tablero[fila][columna] = 0
                    if puntuacion > mejor_puntuacion:
                        mejor_puntuacion = puntuacion
                        mejor_jugada = (fila, columna)
        if mejor_jugada is not None:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = self.raton
            return True
        else:
            return False

    def minimax(self, profundidad, esMaximizador):
        resultado = self.indicarEstado()
        if resultado != 0:
            return resultado

        if esMaximizador:
            mejor_puntuacion = float('-inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = self.raton
                        puntuacion = self.minimax(profundidad + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = max(mejor_puntuacion, puntuacion)
            return mejor_puntuacion
        else:
            mejor_puntuacion = float('inf')
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = self.gato
                        puntuacion = self.minimax(profundidad + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntuacion = min(mejor_puntuacion, puntuacion)
            return mejor_puntuacion

    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2]:
                if self.tablero[fila][0] == self.gato:
                    return 2
                elif self.tablero[fila][0] == self.raton:
                    return 3
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna]:
                if self.tablero[0][columna] == self.gato:
                    return 2
                elif self.tablero[0][columna] == self.raton:
                    return 3
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
        for fila in self.tablero:
            if 0 in fila:
                return 0
        return 1

    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and all(len(fila) == 3 for fila in matriz):
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

         