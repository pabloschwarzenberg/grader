class JuegoDelGato:
    def __init__(self):
        self.tablero = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.turno_gato = True
    
    def jugarGato(self, fila, columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = 1
            self.turno_gato = False
            return True
        else:
            return False
    
    def jugarRaton(self):
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == 0:
                    movimientos.append((i, j))
        
        if len(movimientos) > 0:
            mejor_movimiento = movimientos[0]
            mejor_puntaje = float('-inf')
            
            for movimiento in movimientos:
                self.tablero[movimiento[0]][movimiento[1]] = -1
                puntaje = self.minimax(False)
                self.tablero[movimiento[0]][movimiento[1]] = 0
                
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_movimiento = movimiento
            
            self.tablero[mejor_movimiento[0]][mejor_movimiento[1]] = -1
            self.turno_gato = True
            return True
        else:
            return False
    
    def minimax(self, esMaximizador):
        estado = self.indicarEstado()
        
        if estado == 2:
            return 1
        elif estado == 3:
            return -1
        elif estado == 1:
            return 0
        
        if esMaximizador:
            mejor_puntaje = float('-inf')
            
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = 1
                        puntaje = self.minimax(False)
                        self.tablero[i][j] = 0
                        mejor_puntaje = max(mejor_puntaje, puntaje)
            
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            
            for i in range(3):
                for j in range(3):
                    if self.tablero[i][j] == 0:
                        self.tablero[i][j] = -1
                        puntaje = self.minimax(True)
                        self.tablero[i][j] = 0
                        mejor_puntaje = min(mejor_puntaje, puntaje)
            
            return mejor_puntaje
    
    def mostrar_tablero(self):
        return self.tablero
    
    def cargar_tablero(self, matriz):
        if len(matriz) == 3 and len(matriz[0]) == 3 and len(matriz[1]) == 3 and len(matriz[2]) == 3:
            self.tablero = matriz
    
    def indicarEstado(self):
        for i in range(3):
            # Filas
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != 0:
                return 2 if self.tablero[i][0] == 1 else 3
            
            # Columnas
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != 0:
                return 2 if self.tablero[0][i] == 1 else 3
        
        # Diagonales
        if (self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != 0) or \
                (self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != 0):
            return 2 if self.tablero[1][1] == 1 else 3
        
        # Empate
        if all(self.tablero[i][j] != 0 for i in range(3) for j in range(3)):
            return 1
        
        # Juego en progreso
        return 0
