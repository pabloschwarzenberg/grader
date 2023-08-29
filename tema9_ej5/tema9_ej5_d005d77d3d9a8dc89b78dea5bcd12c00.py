class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            return True
        else:
            return False
    
    def jugarRaton(self):
        mejor_puntaje = -float('inf')
        mejor_fila = -1
        mejor_columna = -1
        
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == 0:
                    self.tablero[fila][columna] = -1
                    puntaje = self.minimax(0, False)
                    self.tablero[fila][columna] = 0
                    
                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_fila = fila
                        mejor_columna = columna
        
        if mejor_fila != -1 and mejor_columna != -1:
            self.tablero[mejor_fila][mejor_columna] = -1
            return True
        else:
            return False
    
    def minimax(self, depth, isMaximizing):
        estado = self.indicarEstado()
        
        if estado != 0:
            return estado
        
        if isMaximizing:
            mejor_puntaje = -float('inf')
            
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = 1
                        puntaje = self.minimax(depth + 1, False)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            
            for fila in range(3):
                for columna in range(3):
                    if self.tablero[fila][columna] == 0:
                        self.tablero[fila][columna] = -1
                        puntaje = self.minimax(depth + 1, True)
                        self.tablero[fila][columna] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            
            return mejor_puntaje
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        self.tablero = matriz
    
    def indicarEstado(self):
        for fila in range(3):
            if self.tablero[fila][0] == self.tablero[fila][1] == self.tablero[fila][2] != 0:
                if self.tablero[fila][0] == 1:
                    return 2  # Ganó el gato
                else:
                    return 3  # Ganó el ratón
        
        for columna in range(3):
            if self.tablero[0][columna] == self.tablero[1][columna] == self.tablero[2][columna] != 0:
                if self.tablero[0][columna] == 1:
                    return 2  # Ganó el gato
                else:
                    return 3  # Ganó el ratón
        
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0:
            if self.tablero[0][0] == 1:
                return 2  # Ganó el gato
            else:
                return 3  # Ganó el ratón
        
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0:
            if self.tablero[0][2] == 1:
                return 2  # Ganó el gato
            else:
                return 3  # Ganó el ratón
        
        if self.tablero_lleno():
            return 1  # Empate
        
        return 0  # Juego en curso
    
    def tablero_lleno(self):
        for fila in self.tablero:
            if 0 in fila:
                return False
        return True
