class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.jugador_actual = 1  # 1 para el gato, -1 para el ratón
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.jugador_actual = -1
            return True
        else:
            return False
    
    def jugarRaton(self):
        mejor_puntaje = None
        mejor_jugada = None

        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(False)
                    self.tablero[fila][columna] = 0

                    if mejor_puntaje is None or puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_jugada = (fila, columna)

        if mejor_jugada is not None:
            fila, columna = mejor_jugada
            self.tablero[fila][columna] = -1
            self.jugador_actual = 1
            return True
        else:
            return False
    
    def minimax(self, es_maximizador):
        estado = self.indicarEstado()

        if estado != 0:
            return estado
        
        if es_maximizador:
            mejor_puntaje = None

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntaje = self.minimax(False)
                        self.tablero[fila][columna] = 0

                        if mejor_puntaje is None or puntaje > mejor_puntaje:
                            mejor_puntaje = puntaje

            return mejor_puntaje
        else:
            peor_puntaje = None

            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntaje = self.minimax(True)
                        self.tablero[fila][columna] = 0

                        if peor_puntaje is None or puntaje < peor_puntaje:
                            peor_puntaje = puntaje

            return peor_puntaje
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        self.tablero = matriz
    
    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                return 2 if self.tablero[fila][0] == 1 else 3
        
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                return 2 if self.tablero[0][columna] == 1 else 3
        
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            return 2 if self.tablero[0][0] == 1 else 3
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            return 2 if self.tablero[0][2] == 1 else 3
        
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    return 0
        
        return 1


# Ejemplo de uso
juego = JuegoDelGato()
juego.jugarGato(0, 0)
juego.jugarRaton()
juego.jugarGato(1, 1)
juego.jugarRaton()
juego.jugarGato(2, 2)
print(juego.mostrar_tablero())
print(juego.indicarEstado())

         